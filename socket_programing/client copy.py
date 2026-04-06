import socket
import pickle
HEADER = 64
PORT = 19661
FORMAT = 'utf-8'
DISCONNECTED_MESSSAGE = '!DISCONNECTED'
SERVER = "0.tcp.in.ngrok.io"
ADDR  = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)    
    send_length += b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send('hello world!')
send('[working]')
send(DISCONNECTED_MESSSAGE)
