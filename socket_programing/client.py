FORMAT = 'utf-8'
PORT = 6060
IP_ADDR = '127.0.0.1'
ADDR = (IP_ADDR,PORT)
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
client.send("hello word! i am in!!".encode(FORMAT))
response = client.recv(1024)
print(f"from server side --> {response}")
client.close()