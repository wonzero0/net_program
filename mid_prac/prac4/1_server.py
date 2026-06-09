# ✅ 9번. TCP Partial Read/Write (15점) ⭐중요
# 문제

# TCP에서 메시지가 한 번에 다 안 올 수 있다.
# 클라이언트가 10바이트 문자열을 보내면 서버는 정확히 10바이트를 모두 수신하여 출력하라

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9001))
server.listen(1)

conn, addr = server.accept()

data = b''
while len(data) < 10:  # 🔥 정확히 10바이트 받을 때까지
    chunk = conn.recv(10 - len(data))
    if not chunk:
        break
    data += chunk

print("수신:", data.decode())
conn.close()