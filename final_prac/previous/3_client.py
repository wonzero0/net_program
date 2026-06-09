import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

while True:
    msg = input("Message to send: ")
    client.send(msg.encode())
    response = client.recv(1024).decode()
    print(response)