import socket
import threading

def handle_client(conn):
    request = conn.recv(1024)
    with open('iot.png', 'rb') as f:
        img_data = f.read()
    
    # HTTP 응답 형식 전송
    response = b"HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n" + img_data
    conn.sendall(response)
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))
server.listen(5)

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn,)).start()


# ============ 멀티스레드 UDP =================
# import socket
# import threading

# def handle_client(data, addr, server_socket):
#     # 'iot.png' 파일 읽기
#     try:
#         with open('iot.png', 'rb') as f:
#             img_data = f.read()
        
#         # UDP로 이미지 데이터와 HTTP 응답 헤더 전송
#         # 주의: UDP는 패킷 크기 제한이 있으므로 큰 이미지는 데이터가 유실될 수 있음
#         response = b"HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n" + img_data
#         server_socket.sendto(response, addr)
#     except Exception as e:
#         print(f"Error handling request from {addr}: {e}")

# # UDP 소켓 생성 (AF_INET, SOCK_DGRAM)
# server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server.bind(('localhost', 8888))

# print("UDP 서버가 대기 중입니다...")

# while True:
#     # 데이터 수신: 클라이언트로부터 패킷을 받음
#     data, addr = server.recvfrom(1024)
    
#     # 수신된 요청을 처리할 스레드 시작
#     threading.Thread(target=handle_client, args=(data, addr, server)).start()