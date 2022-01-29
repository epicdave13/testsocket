import socket
import os

os.startfile('with out at.mp3')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input('ip: ')
port = 65000
server.bind((ip,port))
server.listen(5)
sock, addr = server.accept()
print(f'Succesfully connected [{addr}]')
while True:
    data = input('#: ')
    sock.send(data.encode('utf-8'))
