# ✅ 3번. TCP 소켓 프로그래밍 (15점)

# 클라이언트가 메시지를 보내면 서버가 대문자로 변환하여 응답하는 프로그램 작성

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9000))
server.listen(1)

conn, addr = server.accept()

data = conn.recv(1024)
conn.send(data.upper())

conn.close()