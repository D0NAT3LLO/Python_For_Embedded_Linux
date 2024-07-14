import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
print(f"your ip is : {ip}")
print("=============================")

s.bind((ip,5000))
s.listen(5)

def Handle_clients():
    while True:
        client,address=s.accept() 
        print(f"your are connected to the address{address}")
        threading.Thread(target=send_recv_msg,args=(client,)).start()

def send_recv_msg(client):
    while True :
        rodata=client.recv(1024)
        #sleep(5)
        print(f"{client} is sending you a message which is : {rodata.decode('utf-8')} ")
        #msg=str(input("enter the message that u want to send "))
        msg=("got the message,Thank you!")
        msg_encoded=msg.encode('UTF-8')
        client.send(msg_encoded)
        client.close
    
Handle_clients()
#threading.Thread(target=Handle_clients).start()
