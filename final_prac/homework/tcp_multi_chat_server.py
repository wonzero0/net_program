import socket
import threading

def handle_client(conn, addr):
    # 접속하자마자 ID 수신
    user_id = conn.recv(1024).decode()
    print(f"[알림] {user_id}님이 접속했습니다. ({addr})")
    
    # 다른 클라이언트들에게 입장 알림 전송
    for client in clients:
        if client != conn:
            client.send(f"[알림] {user_id}님이 입장했습니다.".encode())
            
    try:
        while True:
            msg = conn.recv(1024)
            if not msg: break
            # 서버 콘솔에 출력
            print(f"{user_id}: {msg.decode()}")
            # 다른 클라이언트들에게 메시지 전송
            for client in clients:
                if client != conn:
                    client.send(f"{user_id}: {msg.decode()}".encode())
    except:
        pass
    finally:
        clients.remove(conn)
        conn.close()
        print(f"[알림] {user_id}님이 나갔습니다.")

clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 2500))
server.listen(5)
print("TCP 채팅 서버 시작됨")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.daemon = True
    thread.start()