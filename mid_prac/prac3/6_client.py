import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = ('localhost', 9999)

s.settimeout(1)

for i in range(3):
    try:
        print(f"시도 {i+1} 메시지 전송")
        s.sendto(b'Hello', addr)

        data, _ = s.recvfrom(1024)
        print("응답 수신: ", data.decode())
        print("Success")
        break

    except socket.timeout:
        print("Timeout 발생 -> 재전송 시도")

else:
    print("Fail (3번 시도 실패)")

s.close()