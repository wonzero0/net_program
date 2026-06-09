# ✅ 11번. UDP 채팅 프로그램 (15점)
# 문제

# UDP를 이용하여 메시지를 보내면 서버가 그대로 돌려주는 프로그램 작성

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 8888))

while True:
    data, addr = server.recvfrom(1024)
    print("수신: ", data.decode())
    server.sendto(data, addr)

