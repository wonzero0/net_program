import socket
import threading

def receive_msg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data: break
            print(data.decode())
        except:
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 2500))

# ID 입력 및 서버로 즉시 전송
my_id = input('ID를 입력하세요: ')
sock.send(my_id.encode())

# 수신용 스레드 시작
th = threading.Thread(target=receive_msg, args=(sock,))
th.daemon = True
th.start()

# 송신 루프
while True:
    msg = input()
    # 이미 ID를 서버가 알고 있으므로 메시지만 보내도 됨
    sock.send(msg.encode())