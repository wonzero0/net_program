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