import socket

server_addr = ('localhost', 9999)
# 1. SOCK_STREAM (TCP) 사용
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_addr) # 2. 서버와 연결 시도

print("TCP Message Client (Reliable Connection)")

while True:
    user_input = input('Enter message ("send mboxId msg", "receive mboxId", "quit"): ')
    
    # 3. TCP는 운영체제가 재전송을 알아서 하므로 reTx(재전송) 코드가 필요 없습니다!
    try:
        s.sendall(user_input.encode())
        
        data = s.recv(1024)
        print(f"<- {data.decode()}")
        
        if user_input.lower() == 'quit':
            break
    except Exception as e:
        print(f"연결 에러: {e}")
        break

s.close()