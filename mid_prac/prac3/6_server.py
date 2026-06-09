# ✅ 7번. UDP 손실 복구 (10점)
# 문제

# UDP에서 패킷 손실이 발생할 경우 클라이언트 측에서 재전송 로직을 작성하라.

# 조건:

# timeout: 1초
# 최대 3번 전송

import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 9999))

print("UDP 서버 실행 중 ...")

while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode()

    print(f"수신: {msg}")

    if random.random() < 0.25:
        print(">>> 패킷 손실 발생 (응답 X)")
        continue

    s.sendto(b"ACK", addr)
    print(">>> ACK 전송 ")