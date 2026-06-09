from socket import *
import random

port = 5555                                 
s = socket(AF_INET, SOCK_DGRAM)             # 1. SOCK_DGRAM (UDP) 사용
s.bind(('', port))                          # 서버 주소 바인딩

print("UDP Device 1 is running...")

active = True

while active:
    # 2. UDP는 accept() 없이 바로 recvfrom으로 데이터를 받습니다.
    # data는 받은 내용, addr은 클라이언트의 주소(IP, Port)입니다.
    data, addr = s.recvfrom(1024)
    msg = data.decode()
            
    if msg == "quit":                       # 클라이언트에서 quit 메시지가 들어오면
        active = False                      # 서버 종료 준비
        print("종료 요청 수신")
        continue                            # 루프의 처음으로 돌아가 종료 처리

    if msg == "Request":                    # 클라이언트가 데이터를 요구하면 
        temp = random.randint(0, 40)        # 무작위 데이터 생성
        humid = random.randint(0, 100)
        lilum = random.randint(70, 150)

        response = f"Temp = {temp}, Humid = {humid}, lilum = {lilum}"
        
        # 3. 답장을 보낼 때 반드시 받은 주소(addr)를 지정해서 sendto를 사용합니다.
        s.sendto(response.encode(), addr)
        print(f"{addr}로 데이터 전송 완료")

s.close() 
print("Device 1이 종료되었습니다.")