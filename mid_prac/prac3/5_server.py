import socket
import struct
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9999))
s.listen(1)

print("TCP 서버 대기 중...")

while True:
    conn, addr = s.accept() 
    print(f"연결됨: {addr}")

    try:
        while True:
            data = conn.recv(1024)
            if not data: 
                print("클라이언트가 접속을 종료했습니다.")
                break

            id = random.randint(1, 100)
            temp = random.randint(1, 50)
            hum = random.randint(1, 100)
            seq = random.randint(50, 150)

            packet = struct.pack('!HBBI', id, temp, hum, seq)
            conn.send(packet)
    except Exception as e:
        print(f"통신 중 에러 발생: {e}")
    finally:
        conn.close()