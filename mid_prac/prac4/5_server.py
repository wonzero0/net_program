# ✅ 14번. HTTP 요청 파싱 (15점)
# 문제

# 다음 요청에서 q 값을 추출하라.

# GET /exam?q=hello HTTP/1.1

import socket
import struct
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(1)

conn, addr = server.accept()

data = conn.recv(1024)  # Hello 받기

id = random.randint(1, 100)
temp = random.randint(1, 50)
hum = random.randint(1, 100)
seq = random.randint(1, 100000)

packet = struct.pack('!HBBI', id, temp, hum, seq)
conn.send(packet)

conn.close()