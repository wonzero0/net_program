from socket import *

server_addr = ('localhost', 9999)
s = socket(AF_INET, SOCK_STREAM)

try:
    s.connect(server_addr)
    print("TCP Message Client (Type 'quit' to exit)")

    while True:
        user_input = input('Enter message("send mboxId msg" or "receive mboxId"): ')
    
        s.send(user_input.encode())

        if user_input.lower() == 'quit':
            break
            
        data = s.recv(1024)
        if not data:
            print("서버와의 연결이 끊겼습니다.")
            break
            
        print(f"Server response: {data.decode()}")

except Exception as e:
    print(f"연결 오류: {e}")
finally:
    s.close()
    print("Client closed.")