
flag = "jp pj jp pj jp pj jp jp  jp pj pj jp jp jp jp pj  jp pj pj jp pj pj jp pj  jp pj pj jp pj jp jp pj  jp pj pj jp pj pj jp jp  jp pj jp jp jp jp pj pj  jp pj jp pj jp pj jp jp  jp pj jp jp jp pj pj jp  jp pj pj pj pj jp pj pj  jp pj pj pj jp pj pj pj  jp pj pj jp pj jp jp jp  jp jp pj pj jp pj jp jp  jp pj pj pj jp pj jp jp  jp pj jp pj pj pj pj pj  jp pj pj pj jp pj jp jp  jp pj pj jp pj jp jp jp  jp jp pj pj jp jp pj pj  jp pj jp pj pj pj pj pj  jp pj pj jp jp jp pj jp  jp jp pj jp jp jp jp pj  jp jp pj pj jp pj jp jp  jp pj pj pj jp jp pj jp  jp pj pj pj pj jp jp pj  jp pj pj pj pj pj jp pj"
flag = flag.replace("jp", "0")
flag = flag.replace("pj", "1")

flag_ = ""
temp = 0
for x in flag:
	if x == "0" or x == "1":
		temp += 1
		flag_ += x
	if temp == 8 and x == " ":
		flag_ += " "
		temp = 0

print("[+] Binary flag : " + flag_)

# Flag : TamilCTF{wh4t_th3_b!4ry}
