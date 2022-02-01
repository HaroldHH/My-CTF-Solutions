from Crypto.Util.number import long_to_bytes

# 1. Extracted from wireshark manually
vim_encrypt = 0x56696d43727970747e303121d4dfa1d70dc82d3c4abd143cbf51ae292955d8233081e8fa988529088b12a8f0f0c6795a31c39ab3da4ff07b8c95ffc2085c2cbd5065313f930a818b53d277cc658b7da93c724e88e721e4916429e29d
vim_encrypt = long_to_bytes(vim_encrypt)

# 2. Create the encrypted vim file
f = open("test", "wb")
f.write(vim_encrypt)
f.close()

# 3. Use the code from https://github.com/nlitsme/vimdecrypt
# 4. Use rockyou.txt for bruteforce (https://github.com/praetorian-inc/Hob0Rules/blob/master/wordlists/rockyou.txt.gz)
# 5. Try this command `python3 vimdecrypt.py --dictionary rockyou.txt --bruteforce ./test`
# 6. The password is 'samantha'

# Flag : TamilCTF{vi_vii_viiim_lol}

# Reference : https://ctftime.org/writeup/22907
