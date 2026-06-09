from socket import *
import random

port = 6666
s = socket(AF_INET, SOCK_STREAM) # 1. 다시 SOCK_STREAM(TCP)으로 설정
s.bind(('', port))
s.listen(5) # 2. 클라이언트의 접속을 기다리는 대기 줄 생성

print("Device 2 is running...")

active = True 

while active: 
    # 3. 클라이언트의 접속을 수락하여 전용 통로(conn)와 주소(addr)를 받음
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    
    while True:
        # 4. 연결된 통로(conn)를 통해 데이터를 받음
        data = conn.recv(1024).decode()
        
        if not data: # 연결이 끊어지면 내부 루프 종료
            break
        
        if data == 'quit':
            active = False 
            print("Device 2 종료 요청 수신")
            break # 내부 루프를 빠져나가서 active 체크
        
        if data == 'Request':
            # Device 2 데이터 생성
            heart = random.randint(40, 140)
            steps = random.randint(2000, 6000)
            cal = random.randint(1000, 4000)
            
            response = f"Heartbeat={heart}, Steps={steps}, Cal={cal}"
            
            # 5. 연결된 상대방에게 데이터 전송 (주소 적을 필요 없음)
            conn.send(response.encode())
            
    conn.close() # 대화가 끝나면 전용 통로 닫기

s.close()
print("Device 2가 종료되었습니다.")