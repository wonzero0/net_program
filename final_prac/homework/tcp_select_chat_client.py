import socket, threading

def receive_msg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data: break
            print(f"\n{data.decode()}")
        except: break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 2500))

my_id = input('ID를 입력하세요: ')

# 수신 스레드 실행
th = threading.Thread(target=receive_msg, args=(sock,))
th.daemon = True
th.start()

# 송신 루프
while True:
    msg = input()
    sock.send(f"[{my_id}] {msg}".encode())