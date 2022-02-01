import turtle, time

code = "PU,L(180),F(300),PD,R(90),F(50),R(90),F(20),R(180),C(12,-180),R(180),F(20),R(180),F(20),R(180),C(12,-180),R(180),F(20),PU,R(180),F(50),L(90),PD,F(50),R(90),F(30),R(180),F(30),L(90),F(20),L(90),F(20),PU,F(20),L(90),PD,F(20),R(90),F(20),R(180),C(10,-180),R(180),F(20),L(90),F(30),R(180),F(30),R(135),F(45),L(45),PU,F(20),PD,L(90),F(30),L(180),F(15),L(45),F(25),L(180),F(25),R(90),F(25),PU,R(45),F(10),PD,L(90),F(20),R(90),F(30),L(180),F(30),L(90),F(35),C(17,-270),R(180),F(17),PU,R(180),F(50),L(90),PD,F(35),R(180),F(12),C(11,-180),R(180),F(30),PU,L(90),F(30),PD,C(30,170),C(20,360),PU,L(188),F(30),R(47),PD,F(35),L(98),F(35),L(180),F(35),L(42),F(30)"
code_split = code.split(",")

print(code_split)

new_code = []
temp = ""
for x in code_split:
	if "(" in x and ")" in x:
		new_code.append(x)
	elif "(" not in x and ")" not in x:
		new_code.append(x)
	else:
		if "(" in x:
			temp += x + ","
		else:
			temp += x
	if "(" in temp and ")" in temp:
		new_code.append(temp)
		temp = ""

print("")
print(new_code)

screen = turtle.Turtle()
for x in new_code:
        if "PU" in x:
                code = x.replace("PU", "screen.penup()")
                eval(code)
        if "L" in x:
                code = x.replace("L", "screen.left")
                eval(code)
        if "R" in x:
                code = x.replace("R", "screen.right")
                eval(code)
        if "F" in x:
                code = x.replace("F", "screen.forward")
                eval(code)
        if "PD" in x:
                code = x.replace("PD", "screen.pendown()")
                eval(code)
        if "C" in x:
                code = x.replace("C", "screen.circle")
                eval(code)
        #time.sleep(1)

# The result is BFRk5n9Y and find it in pastebin
# TamilCTF{7urtl3s_4r3_veRrrRyy_sl0ww}
