import socket
import select
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(5)
inputs = [server]

while True:
    readable, _, _ = select.select(inputs, [], [])
    for s in readable:
        if s is server:
            conn, addr = s.accept()
            inputs.append(conn)
        else:
            data = s.recv(1024).decode().strip()
            if data == '1':
                s.send(f"Temp={random.randint(0, 40)}".encode())
            elif data == '2':
                s.send(f"Humid={random.randint(0, 100)}".encode())
            else:
                s.close()
                inputs.remove(s)


# ============= selectors 모듈로 변환한 TCP 서버 코드 ==========
# import selectors
# import socket
# import random

# # DefaultSelector를 사용하여 운영체제에 가장 적합한 방식을 자동으로 선택합니다.
# sel = selectors.DefaultSelector()

# def accept(sock, mask):
#     """서버 소켓에 연결 요청이 들어왔을 때 실행되는 함수"""
#     conn, addr = sock.accept()
#     print(f"연결됨: {addr}")
#     conn.setblocking(False) # 비블로킹 모드 설정
#     # 새로운 클라이언트 소켓을 '읽기' 이벤트로 등록
#     sel.register(conn, selectors.EVENT_READ, read)

# def read(conn, mask):
#     """클라이언트 소켓에서 데이터를 수신했을 때 실행되는 함수"""
#     try:
#         data = conn.recv(1024).decode().strip()
#         if data == '1':
#             conn.send(f"Temp={random.randint(0, 40)}".encode())
#         elif data == '2':
#             conn.send(f"Humid={random.randint(0, 100)}".encode())
#         else:
#             # 유효하지 않은 데이터이거나 연결 종료 요청 시
#             print("연결 종료")
#             sel.unregister(conn)
#             conn.close()
#     except Exception:
#         sel.unregister(conn)
#         conn.close()

# # 서버 소켓 설정
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('localhost', 9999))
# server.listen(5)
# server.setblocking(False) # 서버 소켓도 비블로킹으로 설정

# # 서버 소켓을 '읽기' 이벤트 발생 시 'accept' 함수가 실행되도록 등록
# sel.register(server, selectors.EVENT_READ, accept)

# print("Selectors 서버 가동 중...")

# while True:
#     # 이벤트가 발생할 때까지 대기
#     events = sel.select()
#     for key, mask in events:
#         callback = key.data  # 등록할 때 넘겨준 함수(accept 또는 read)
#         callback(key.fileobj, mask) # 해당 함수 호출


# ========== 멀티스레드 사용 --------------
# import socket
# import threading
# import random

# def handle_client(conn):
#     try:
#         while True:
#             data = conn.recv(1024).decode().strip()
#             if data == '1':
#                 conn.send(f"Temp={random.randint(0, 40)}".encode())
#             elif data == '2':
#                 conn.send(f"Humid={random.randint(0, 100)}".encode())
#             else:
#                 # 연결 종료 조건
#                 break
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         conn.close()

# # 서버 설정
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('localhost', 9999))
# server.listen(5)
# print("Server is running on port 9999...")

# while True:
#     conn, addr = server.accept()
#     # 클라이언트가 접속할 때마다 새로운 스레드 생성
#     client_thread = threading.Thread(target=handle_client, args=(conn,))
#     client_thread.start()