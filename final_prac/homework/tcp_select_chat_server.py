import socket, select

socks = []
BUFFER = 1024
PORT = 2500

s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print(f"TCP 채팅 서버 시작됨: {PORT}번 포트 대기 중")

while True:
    # 읽기 가능한 소켓들만 골라냄
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    for s in r_sock:
        # 1. 서버 소켓이면 새로운 접속
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print(f"[{addr}]님 접속")
        
        # 2. 클라이언트 소켓이면 메시지 처리
        else:
            try:
                data = s.recv(BUFFER)
                if not data: # 접속 종료
                    s.close()
                    socks.remove(s)
                    continue
                
                # 나를 제외한 모든 클라이언트에게 메시지 전송
                msg = data.decode()
                print(f"수신: {msg}")
                for client in socks:
                    if client != s_sock and client != s:
                        client.send(msg.encode())
            except:
                s.close()
                socks.remove(s)