import socket
import random
import struct 
host = 'localhost'
port = 9999 

# 1. TCP 소켓 및 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)

print(f"TCP IoT 서버 시작... ({host}:{port})")

while True:
    conn, addr = sock.accept()
    print(f"클라이언트 연결됨: {addr}")

    try:
        while True:
            data = conn.recv(1024)
            if not data: break
            
            request = data.decode()
            temp, humid, lumi = 0, 0, 0

            if request == '1':
                temp = random.randint(1, 50)
            elif request == '2':
                humid = random.randint(1, 100)
            elif request == '3':
                lumi = random.randint(1, 150)

            response = struct.pack('!HHH', temp, humid, lumi)
            
            conn.send(response)
            print(f"전송 데이터: Temp={temp}, Humid={humid}, Lumi={lumi}")
            
    except Exception as e:
        print(f"에러 발생: {e}")
    finally:
        conn.close() # 통신 종료 후 연결 닫기