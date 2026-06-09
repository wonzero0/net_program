from socket import *
import time 

server_addr = ('localhost', 7000)                   # 서버의 주소를 localhost, port 번호를 7000으로 지정 

client_sock = socket(AF_INET, SOCK_STREAM)
client_sock.connect(server_addr)                    # 서버의 주소에 맞게 연결 

for i in range(3):                                  # 3번 반복
    start_time = time.time()                        # 시작 시간 측정 
    client_sock.send('ping'.encode())               # 서버에게 ping을 바이트로 변환하여 전송 
    
    data = client_sock.recv(1024)  
    end_time = time.time()                          # 끝나는 시간 측정 
    
    if data.decode() == 'pong':                     # 받은 데이터를 문자열로 바꾸었을 때 pong 이 맞다면 
        rtt = end_time - start_time                 # 끝나는 시간 - 시작 시간을 계산하여 서버까지 갔다 오는데 걸리는 시간을 측정 
        print(f"Success (RTT: {rtt:.6f})")          # 소수점 6자리까지만 출력 

client_sock.close() 