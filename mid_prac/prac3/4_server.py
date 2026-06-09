# ✅ 4번. UDP + struct pack/unpack (15점) 🔥핵심

# 다음 조건을 만족하는 프로그램을 작성하라.

# 조건
# 클라이언트 → 서버: "REQ"
# 서버 → 클라이언트:
# 온도 (2바이트)
# 습도 (2바이트)

# 👉 struct 사용 필수

import socket
import struct
import random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 9999))

while True:
    data, addr = s.recvfrom(1024)

    temp = random.randint(1, 50)
    hum = random.randint(1, 100)

    packet = struct.pack('!hh', temp, hum)
    s.sendto(packet, addr)
