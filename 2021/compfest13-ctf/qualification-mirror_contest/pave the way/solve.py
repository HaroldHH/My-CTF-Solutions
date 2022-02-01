import re

def recursive_finder(next_file_name, current_flag, current_char):
    if current_char == "}":
        if re.match("COMPFEST13\{[A-z0-9_-]+\}", current_flag) != None:
            print("[+] Flag : " + current_flag)
            return
        else:
            return
    else:
        try:
            f = open(next_file_name, "r")
        except:
            return
        char_value = ""
        next_files = []
        for y in f:
            result = re.findall(r"var0 \= var0 \+ \".\"", y)
            next_target = re.findall(r"c[0-9]*\.pave\(var0\)", y)
            if result != []:
                a,b = result[0].split("+")
                target = b.replace("\"", "")
                target = target.replace(" ", "")
                char_value = target
            if next_target != []:
                next_file_name_ = next_target[0].replace("pave(var0)", "java")
                next_files.append(next_file_name_)
            if "Done" in y:
                print("[+] Flag : " + current_flag + char_value)
                return
        #print("[+] " + char_value + ", c" + str(x) + ".java => " + next_file)
        f.close()
        curr_flag = current_flag + char_value
        for next_file in next_files:
            # Remove comment dibawah untuk liat prosesnya
            #print("./"+next_file + " " + curr_flag + " " + char_value)
            recursive_finder("./"+next_file, curr_flag, char_value)

for x in range(0,999):
    f = open("./c"+str(x)+".java", "r")
    char_value = ""
    for y in f:
        result = re.findall(r"var0 \= var0 \+ \".\"", y)
        next_target = re.findall(r"c[0-9]*\.pave\(var0\)", y)
        if result != []:
            a,b = result[0].split("var0 + ")
            target = b.replace("\"", "")
            if target == "C":
                char_value = target
            else:
                char_value = ":))"
        if next_target != []:
            next_file_name_ = next_target[0].replace("pave(var0)", "java")
    if char_value != ":))":
        #print("[+] "+char_value+", " + "./c"+str(x)+".java" + " => " + next_file_name_)
        recursive_finder(next_file_name_, "C", "C")
