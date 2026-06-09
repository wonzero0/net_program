from socket import *
import random

port = 5555                                 
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(5)

print("Device 1 is running...")

active = True                                   # 서버 전체를 켜두는 코드 

while active:                                   # 서버가 켜져 있는 동안 무한 반복 
    conn, addr = s.accept()                     # 접속을 받음 
    while True:                     
        data = conn.recv(1024).decode()         # 클라이언트가 보낸 데이터를 문자열로 바꿔서 받음 
        if not data:                            # 예외 처리 -> 비정상적인 연결일 시 연결 끊기
            break
            
        if data == "quit":                      # 클라이언트에서 quit라는 문구가 들어오면 
            active = False                      # 서버 끄기
            break   

        if data == "Request":                       # 클라이언트가 데이터를 요구하면 
            temp = random.randint(0, 40)            # 무작위로 온도, 조도, 습도를 생성 
            humid = random.randint(0, 100)
            lilum = random.randint(70, 150)

            response = (f"Temp = {temp}, Humid = {humid}, lilum = {lilum}")
            conn.send(response.encode())            # 바이트로 변경하여 클라이언트에게 전송 

    conn.close()

s.close() 
print("Device 1이 종료되었습니다.")