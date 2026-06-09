import socket

# 1. UDP 소켓 생성 (SOCK_DGRAM)
server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind(('localhost', 7000))

print("UDP Ping 서버 시작 (port 7000)...")

while True:
    # 2. 클라이언트로부터 데이터와 주소 수신
    data, addr = server_sock.recvfrom(1024)
    msg = data.decode()

    # 3. 'ping' 메시지인지 확인 후 'pong' 응답
    if msg == 'ping':
        server_sock.sendto('pong'.encode(), addr)
        print(f"[{addr}] ping 수신 -> pong 전송")