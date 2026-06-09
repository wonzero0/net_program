from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

print("--- TCP Calculator Client ---")
print("입력 예시: 20 + 17 (종료하려면 'q' 입력)")

while True: 
    msg = input("계산식 입력: ")
    
    s.send(msg.encode())

    if msg.lower() == 'q':
        break
    
    try:
        data = s.recv(1024)
        if not data:
            print("서버와 연결이 끊겼습니다.")
            break
        print(f"결과: {data.decode()}")
    except Exception as e:
        print(f"수신 에러: {e}")
        break

s.close()
print("프로그램을 종료합니다.")


# ================UDP 연결일 때===========
# from socket import *

# server_addr = ('localhost', 3333)
# # 1. UDP 소켓 생성 (SOCK_DGRAM)
# s = socket(AF_INET, SOCK_DGRAM)

# print("--- UDP Calculator Client ---")
# print("입력 예시: 20 + 17 (종료하려면 'q' 입력)")

# while True: 
#     msg = input("계산식 입력: ")
    
#     # 2. UDP는 연결이 없으므로 보낼 때마다 목적지 주소를 함께 보냄
#     s.sendto(msg.encode(), server_addr)

#     if msg.lower() == 'q':
#         break
    
#     try:
#         # 3. 서버로부터 응답 대기 (2초 타임아웃 설정을 추가하면 더 좋습니다)
#         s.settimeout(2.0)
#         data, addr = s.recvfrom(1024)
#         print(f"결과: {data.decode()}")
#     except timeout:
#         print("서버로부터 응답이 없습니다. (Timeout)")
#     except Exception as e:
#         print(f"수신 에러: {e}")
#         break

# s.close()
# print("프로그램을 종료합니다.")