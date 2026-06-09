import socket
import random

port = 3333
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

print("채팅 서버 시작...")

while True:
    sock.settimeout(None)                      
    while True: 
        data, addr = sock.recvfrom(BUFF_SIZE)         

        if random.random() <= 0.3:                
            continue                                  
        else:
            sock.sendto(b'ack', addr)                
            print(f'<- {data.decode()}')                
            break   

    msg = input('-> ')
    reTx = 0
    while reTx <= 3:                                   
        resp = str(reTx) + ' ' + msg                 
        sock.sendto(resp.encode(), addr)        
        sock.settimeout(1)                           
        
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
            if data.decode() == 'ack':
                break  
        except socket.timeout:                         
            reTx += 1
            print(f"타임아웃 발생! 재전송 횟수: {reTx}")
            continue

    if reTx > 3:
        print("최대 재전송 횟수를 초과하여 전송에 실패했습니다.")