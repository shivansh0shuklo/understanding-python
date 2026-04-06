import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

FORMAT = 'utf-8'
PORT = 6060
IP_ADDR = '0.0.0.0'
ADDR = (IP_ADDR,PORT)

server.bind(ADDR)
server.listen(5)
print(f"server is listening to port --> {PORT}")
connected = True
while connected:
    try:
        client,addr = server.accept()
        print(f'[connected] to {addr}')
        data = client.recv(1024)
        print(f'[recived data] - {data.decode(FORMAT)}')
        client.send('[message recived]'.encode(FORMAT))
        connected = False
    except Exception as e:
        print(f"[not connected] [{e}]")
        connected = False
    client.close()

    