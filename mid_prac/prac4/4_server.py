# ✅ 13번. TCP 멀티 클라이언트 (기초) (15점)
# 문제

# 여러 클라이언트 접속을 처리하는 TCP 서버 작성 (thread 사용)

import socket
import threading

def handle_client(conn):
    data = conn.recv(1024)
    print("클라이언트:", data.decode())
    conn.send(b'OK')
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 7777))
server.listen(5)

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn,)).start()