import socket
import time
import random

server_addr = ('localhost', 7000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



for i in range(1, 3):
    sock.sendto('ping'.encode(), server_addr)
    send_time = time.time()
    
    try:
        data, addr = sock.recvfrom(1024)
        end_time = time.time()
        
        if data.decode() == 'pong':
            rtt = end_time - send_time
            print(f"Success (RTT: {rtt:.6f})")
        else:
            print("Fail")
            
    except Exception as e:
        print(f"Error: {e}")

    reTx = 0
    while reTx <= 1:
        resp = str(reTx) + ' ' 
        sock.sendto(resp.encode(), server_addr)
        sock.settimeout(2)  
        
        try:
            data, addr = sock.recvfrom(1024)
            if data.decode() == 'ack':
                break
        except socket.timeout:
            reTx += 1
            print(f"타임아웃 발생! 재전송 횟수: {reTx}")
            continue

    if reTx > 1:
        print("최대 재전송 횟수를 초과하여 전송에 실패했습니다.")
    

    sock.close()