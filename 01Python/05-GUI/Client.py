import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
print(f"your ip is : {ip}")
client.connect((ip,5000))
print("================================")
while True:
    msg=str(input("please enter the message: "))
    msg_encoded=msg.encode('UTF-8')
    client.send(msg_encoded)
    print("================================")
    rodata=client.recv(1024)
    print(f"{ip} is sending u a msg :  {rodata.decode('UTF-8')}")
    #client.close()  #closing will lead to Broken Pipe Error in Server!!


