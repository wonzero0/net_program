from socket import *
import random

port = 6666
s = socket(AF_INET, SOCK_DGRAM) # 1. SOCK_DGRAM으로 설정하여 UDP 소켓 생성
s.bind(('', port))

print("UDP Device 2 is running...")

active = True 

while active: 
    # 2. UDP는 accept() 없이 바로 데이터를 받습니다.
    # data는 받은 내용, addr은 답장을 보낼 때 필요한 클라이언트의 주소입니다.
    data, addr = s.recvfrom(1024)
    msg = data.decode()
    
    if not msg:
        break
    
    if msg == 'quit':
        active = False 
        print("Device 2 종료 요청 수신")
        continue # 루프를 돌아 active 조건 확인 후 종료
    
    if msg == 'Request':
        # Device 2의 데이터: 심박수, 걸음수, 칼로리
        heart = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)
        
        response = f"Heartbeat={heart}, Steps={steps}, Cal={cal}"
        
        # 3. 답장을 보낼 때는 반드시 수신된 addr로 전송(sendto)합니다.
        s.sendto(response.encode(), addr)
        print(f"[{addr}]에게 건강 데이터 전송 완료")

s.close()
print("UDP Device 2가 종료되었습니다.")