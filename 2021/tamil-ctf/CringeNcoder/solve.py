import http.client, re

all_encode = "cringe cr1nge cRinge crIng3 cRimG3 cR1Ng3e criNgee CRINGE crinGE ccR1nge CriNGE cRINGe cr1ngE cringE CRIng3 Cr1nGe cR1nnge cR1Ng3 CrInGe cRingE cR1NGE CRiNg3 CRINGe CR1NGe cring3 CRIMNGE cRInGE crinG3 cRInge cRinG3 criNG3 cr1NG3 crinGe cRiNge CrInGE CRinGE"
all_encode_arr = all_encode.split(" ")

encode_dict = {}
for x in range(ord('a'), ord('z')+1):
	encode_dict[chr(x)] = all_encode_arr[x-97]
for x in range(ord('0'), ord('9')+1):
	encode_dict[chr(x)] = all_encode_arr[26+(x-48)]

#print(all_encode_arr)
#print(encode_dict)

enc_flag = "cR1Ng3e crinG3 cringE cringe cRINGe cRINGe cring3 crinG3 cringE cringE cRinG3 Cr1nGe cRimG3 criNG3 cRinge cRimG3 cringe cR1Ng3e cRiNge cRinG3 cR1Ng3 CrInGe cRInGE cr1ngE criNG3 cringE cring3 cRinge cR1Ng3 crinGE cringE criNgee cRinG3 CrInGe"
enc_flag_arr = enc_flag.split(" ")

flag = ""
for x in enc_flag_arr:
	for y in encode_dict:
		if encode_dict[y] == x:
			flag += y

print("TamilCTF{"+flag+"}")
