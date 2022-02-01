dna = "TGGC TCAT TGAC TCTA TGTG TCGC TGGT TCTA TCAC TTCC TGAG TGAT TCAC TGGT TGAC TGAT ACAT ACAT TCGT TTCC TGAG TGAT TCAC TGTT TTCC TGTG TGCC TCTT TCAG TCCT"
base_4 = {
	"A" : 0,
	"T" : 1,
	"G" : 2,
	"C" : 3
}

flag = ""
dna_ = dna.split(" ")
for x in dna_:
	c = 0
	c += 64 * base_4[x[0]] # 4th character / left most
	c += 16 * base_4[x[1]]
	c += 4 * base_4[x[2]]
	c += 1 * base_4[x[3]] # 1st charracter / right most
	flag += chr(c)

print("[+] Flag : " + flag)
