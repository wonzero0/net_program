import socket
import random

port = 3333
BUFF_SIZE = 1024
server_addr = ('localhost', port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("채팅 클라이언트 시작...")

while True:
    msg = input('-> ')
    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), server_addr)
        sock.settimeout(2)  
        
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
            if data.decode() == 'ack':
                break
        except socket.timeout:
            reTx += 1
            print(f"타임아웃 발생! 재전송 횟수: {reTx}")
            continue

    if reTx > 5:
        print("최대 재전송 횟수를 초과하여 전송에 실패했습니다.")


    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
       
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print(f'<- {data.decode()}')
            break