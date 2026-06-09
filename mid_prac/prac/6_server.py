import socket
import random

port = 5050
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

print(f"TCP IoT 서버 시작... (Port: {port})")

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    
    if data.decode() == 'Hello':                    # 클라이언트가 보낸 데이터가 Hello 라는 문자열이 맞다면 
    
        sender_id = random.randint(1, 50000)   # 2바이트    -> 송신자 id를 1~50,000 사이의 숫자를 정수 값으로 랜덤 생성 
        receiver_id = random.randint(1, 50000) # 2바이트    -> 수신사 id도 위와 같음 
        lumi = random.randint(1, 100)          # 1바이트    -> 조도, 습도, 온도, 기압은 1~100 사이의 정수 값으로 랜덤 생성 
        humi = random.randint(1, 100)          # 1바이트
        temp = random.randint(1, 100)          # 1바이트
        air = random.randint(1, 100)           # 1바이트    
        seq = random.randint(1, 100000)        # 4바이트    -> 순서 번호는 1~100,000 사이의 정수 값으로 랜덤 생성 

        b_sender = sender_id.to_bytes(2, 'big')           # 위에서 생성된 값들은 2바이트 크기의 이진 데이터로 변환하는데 빅엔디안 방식을 따름 
        b_receiver = receiver_id.to_bytes(2, 'big')       # 위와 동일함
        b_lumi = lumi.to_bytes(1, 'big')
        b_humi = humi.to_bytes(1, 'big')
        b_temp = temp.to_bytes(1, 'big')
        b_air = air.to_bytes(1, 'big')
        b_seq = seq.to_bytes(4, 'big')

        packet = b_sender + b_receiver + b_lumi + b_humi + b_temp + b_air + b_seq   
        # 모든 바이트 조각을 순서대로 이어 붙여 총 12바이트짜리 데이터를 만듦 
        

         # packet = struct.pack('!HHBBBBI', sender_id, receiver_id, lumi, humi, temp, air, seq) -> struct로 할 떄
        conn.send(packet)       # 위에서 만든 패킷을 클라이언트로 전송 
        print(f"데이터 전송 완료: Sender:{sender_id}, Seq:{seq}")
    
    conn.close()