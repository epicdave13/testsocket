import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input('ip: ')
port = 65000
client.connect((ip,port))
while True:
    data = client.recv(1024)
    print(data.decode('utf-8'))