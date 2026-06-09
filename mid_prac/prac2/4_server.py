import socket
import random

port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', port))

print("신뢰성 테스트 UDP 서버 대기 중...")

while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode()

    if random.random() <= 0.25:                                         # 25% 확률로 손실 시키는 코드 임의로 작성 
        print(f"!!! 데이터 손실 시뮬레이션: {msg} 무시 !!!")
        continue

    print(f"[{addr}] 수신 메시지: {msg}")

    response = "ACK: " + msg
    s.sendto(response.encode(), addr)
    print(f"-> 확인 응답(ACK) 전송 완료")