from socket import *

server_addr = ('localhost', 9999)
s = socket(AF_INET, SOCK_DGRAM)

print("UDP Message Client (Type 'quit' to exit)")

while True:
    user_input = input('Enter the message("send mboxId message" or "receive mboxId"): ')
    
    s.sendto(user_input.encode(), server_addr)

    if user_input.lower() == 'quit':
        break
        
    data, addr = s.recvfrom(1024)
    print(data.decode())

s.close()
print("Client closed.")


# ==========TCP=========
# from socket import *

# server_addr = ('localhost', 9999)
# # 1. TCP 소켓 생성 및 서버 연결
# s = socket(AF_INET, SOCK_STREAM)

# try:
#     s.connect(server_addr)
#     print("TCP Message Client (Type 'quit' to exit)")

#     while True:
#         user_input = input('Enter message("send mboxId msg" or "receive mboxId"): ')
        
#         # 2. 연결된 서버로 데이터 전송
#         s.send(user_input.encode())

#         if user_input.lower() == 'quit':
#             break
            
#         # 3. 서버의 대답 수신
#         data = s.recv(1024)
#         if not data:
#             print("서버와의 연결이 끊겼습니다.")
#             break
            
#         print(f"Server response: {data.decode()}")

# except Exception as e:
#     print(f"연결 오류: {e}")
# finally:
#     s.close()
#     print("Client closed.")