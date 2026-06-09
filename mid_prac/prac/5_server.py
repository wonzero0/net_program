from socket import *

port = 7000                                      # 포트번호 7000 으로 지정 

server_sock = socket(AF_INET, SOCK_STREAM)
server_sock.bind(('', port))
server_sock.listen(1)                            # 최대 접속 수 1

print("Ping 서버가 대기 중입니다...")

while True:
    conn, addr = server_sock.accept()
    
    for _ in range(3):                              # 3번 반복 
        data = conn.recv(1024)
        if not data: break
        
        msg = data.decode()                         # 데이터를 문자열로 변환
        if msg == 'ping':                           # 받은 데이터가 ping 이 맞으면 pong을 바이트 형태로 변환하여 전송 
            conn.send('pong'.encode()) 
            
    conn.close()