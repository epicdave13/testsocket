import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input('ip: ')
port = 65000
client.connect((ip,port))
while True:
    data = client.recv(1024)
    if data.decode('utf-8').split()[0] == '#IMAGE#':
        with open(f"{data.decode('utf-8').split()[0]}",'ab') as img:
            imgData = client.recv(1024)
                while imgData:
                    img.write(imgData)
                    imgData = client.recv(1024)
                
    print(data.decode('utf-8'))