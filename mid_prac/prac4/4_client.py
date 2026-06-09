import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 7777))

client.send(b'Hello Server')
data = client.recv(1024)

print("서버 응답:", data.decode())
client.close()