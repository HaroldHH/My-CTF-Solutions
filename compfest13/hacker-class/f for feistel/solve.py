from Crypto.Hash import MD5

# Flag : COMPFEST13{__xor__c4Nc3lation__}

def encrypt(plaintext):
    length = len(plaintext)
    left = plaintext[:length // 2]
    print("[*] First left : " + str(left))
    right = plaintext[length // 2:]
    print("[*] First right : " + str(right))
    keys = [line[:16] for line in open('keys.txt', 'rb').readlines()]
    ciphertext = b''
    for key in keys:
        print("[*] \tleft : " + str(left))
        print("[*] \tright : " + str(right))
        print("[*] \tKey : " + str(key))
        assert len(key) == 16
        tmp = right
        print("[*] \ttmp : " + str(tmp))
        right = xor(right, key)
        print("[*] \t\tright = XOR : " + str(right))
        h = MD5.new()
        h.update(right)
        right = h.hexdigest().encode()
        print("[*] \t\tright = MD5 : " + str(right))
        print("[*] \t\tleft = " + str(left))
        left = xor(left, right)
        print("[*] \t\tleft = XOR : " + str(left))
        right = left
        print("[*] \tright = left : " + str(right))
        left = tmp
        print("[*] \tleft = tmp : " + str(left))
        print("-"*70)
    print("[*] Final result : " + str(right + left))
    return right+left

def decrypt(plaintext):
    length = len(plaintext)
    right = plaintext[:length // 2]
    print("[*] First left : " + str(right))
    left = plaintext[length // 2:]
    print("[*] First right : " + str(left))
    keys = [line[:16] for line in open('keys.txt', 'rb').readlines()][::-1]
    ciphertext = b''
    for key in keys:
        print("[*] \tleft : " + str(left))
        print("[*] \tright : " + str(right))
        print("[*] \tKey : " + str(key))
        assert len(key) == 16
        tmp = left
        print("[*] \ttmp : " + str(tmp))
        left = xor(left, key)
        print("[*] \t\tleft = XOR : " + str(left))
        h = MD5.new()
        h.update(left)
        left = h.hexdigest().encode()
        print("[*] \t\tleft = MD5 : " + str(left))
        print("[*] \t\tright = " + str(right))
        right = xor(right, left)
        print("[*] \t\tleft = XOR : " + str(right))
        left = right
        print("[*] \tleft = right : " + str(left))
        right = tmp
        print("[*] \tright = tmp : " + str(right))
        print("-"*70)
    print("[*] Final result : " + str(left + right))
    return left+right

def xor(a, b):
    ciphertext = b''
    l_a = len(a)
    l_b = len(b)
    for i in range(l_a):
        ciphertext += str(chr(a[i % l_a] ^ b[i % l_b])).encode()
    return ciphertext

'''
flag = "COMPFEST13{" + "A"*20 + "}"
assert len(flag) == 32
enc_flag = encrypt(flag.encode())
print(enc_flag)
print("\n" + "- "*10 + "DECRYPT" + " -"*10 + "\n")
print(decrypt(enc_flag))
'''

encrypted_flag = open('encrypted.txt', 'rb').read()
assert len(encrypted_flag) == 32
print("[*] Flag : " + decrypt(encrypted_flag).decode())
