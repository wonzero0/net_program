from socket import * 
import sys                                  # sys 라이브러리 : 파이썬 인터프리터와 시스템을 연결해주는 통로

port = 2500                                 # 명령어에 포트 번호가 지정되지 않을 때 기본적인 포트번호
BUFSIZE = 1024

if len(sys.argv) > 1:                       # sys.argv : 프로그램을 실행할 때 뒤에 따라오는 옵션값들의 리스트
    port = int(sys.argv[1])                 # python cmd_server.py 5555 라고 입력이 들어왔을 때 [0] = cmd_server, [1] = 5555

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)                      
conn, addr = sock.accept()
print('connected by', addr)

while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break

    print('Received message: ', data.decode())
    conn.send(data)

conn.close()