import socket
import time

server_addr = ('localhost', 7000)
# 1. UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 총 3번 반복 수행
for i in range(3):
    start_time = time.time() # 보내기 전 시간 기록
    
    # 3. 'ping' 메시지 전송
    sock.sendto('ping'.encode(), server_addr)
    
    try:
        # 응답 대기 (UDP는 유실될 수 있으므로 타임아웃 설정을 권장하지만, 
        # 문제 조건에 따라 일단 기본 수신으로 작성합니다.)
        data, addr = sock.recvfrom(1024)
        end_time = time.time() # 받은 후 시간 기록
        
        if data.decode() == 'pong':
            rtt = end_time - start_time
            print(f"Success (RTT: {rtt:.6f})")
            
    except Exception as e:
        print(f"Error: {e}")

# 3회 반복 후 종료
sock.close()