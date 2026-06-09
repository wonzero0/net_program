import socket
import random

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind(('localhost', 7000))

print("UDP Ping 서버 시작 (port 7000)...")

while True:
    data, addr = server_sock.recvfrom(1024)
    msg = data.decode()

    if msg == 'ping':
        if random.random() <= 0.3:
            continue
        else:
            server_sock.sendto('pong'.encode(), addr)
            print(f"[{addr}] ping 수신 -> pong 전송")


socket.close()

        
