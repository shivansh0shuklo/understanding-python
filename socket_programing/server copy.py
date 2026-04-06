import socket
import threading
import time

FORMAT = 'utf-8'
HEADER = 64  
port  =5051
SERVER = "0.0.0.0"
#or
# SERVER = socket.gethostbyname(socket.gethostname())

DISCONNECTED_MESSAGE = "!DISCONNECTED" 

print(socket.gethostname())
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)# just represents the address that it represents
addr  =(SERVER,port)
server.bind(addr)

def handel_client(conn,addr):
    print(f"[new connection] {addr} conected")
    connected  =True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECTED_MESSAGE:
                connected  =False
            print(f"[{addr}] {msg}")
            conn.send("msg recived".encode(FORMAT))
    conn.close()    

def start():#hande new connection and distibute where they need to go 
    server.listen()
    print(f"[listening] server is listening on {SERVER}")
    while True:
        conn,addr = server.accept()
        #conn is a socket object which will help in connection with the client
        thread = threading.Thread(target=handel_client,args=(conn,addr))
        thread.start()
        print(f"[active connections] {threading.active_count() - 1}")


print("[starting] server is starting....")
start()




