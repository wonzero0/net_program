import socket
import struct

server_addr = ('localhost', 9999)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(server_addr)
    print("서버에 연결되었습니다.")

    while True:
        msg = input("측정 정보 선택 (1:온도, 2:습도, 3:조도, q:종료): ")
        
        if msg == 'q': break
        if msg not in ['1', '2', '3']: continue 

        sock.send(msg.encode())

        data = sock.recv(6)
        if not data: break

        temp, humid, lumi = struct.unpack('!HHH', data)

        print(f"수신 결과: Temp={temp}, Humid={humid}, Lumi={lumi}")

except Exception as e:
    print(f"서버 연결 오류: {e}")
finally:
    sock.close()
    print("연결이 종료되었습니다.")