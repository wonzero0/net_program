import socket
import random
import struct

port = 5050
# 1. UDP 통신 정의
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

print(f"UDP IoT 서버 시작... (Port: {port})")

while True:
    # 2. accept() 대신 recvfrom() 사용 (데이터와 상대방 주소를 동시에 받음)
    data, addr = sock.recvfrom(1024)
    
    if data.decode() == 'Hello':
        sender_id = random.randint(1, 50000)
        receiver_id = random.randint(1, 50000)
        lumi = random.randint(1, 100)
        humi = random.randint(1, 100)
        temp = random.randint(1, 100)
        air = random.randint(1, 100)
        seq = random.randint(1, 100000)

        packet = struct.pack('!HHBBBBI', sender_id, receiver_id, lumi, humi, temp, air, seq)

        # struct 사용 안할 떄 
        # packet = (
        #     sender_id.to_bytes(2, 'big') + 
        #     receiver_id.to_bytes(2, 'big') + 
        #     lumi.to_bytes(1, 'big') + 
        #     humi.to_bytes(1, 'big') + 
        #     temp.to_bytes(1, 'big') + 
        #     air.to_bytes(1, 'big') + 
        #     seq.to_bytes(4, 'big')
        # )

        sock.sendto(packet, addr)
        print(f"[{addr}] 데이터 전송 완료: Sender:{sender_id}, Seq:{seq}")