import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9001))

client.send(b'abcdefghij')  # 10바이트
client.close()