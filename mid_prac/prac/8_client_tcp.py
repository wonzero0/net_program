import socket

server_addr = ('localhost', 6789)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1. TCP 소켓
sock.connect(server_addr) # 2. 서버에 접속

# 서버에게 Hello 전송
sock.send(b'Hello')

data = sock.recv(1024)
if data.decode() == 'Filename':
    fname = input("받고 싶은 파일 이름을 입력하세요: ")
    sock.send(fname.encode())
    
    # 3. 파일 내용 수신
    # TCP는 데이터가 쪼개져서 올 수 있으므로 충분한 크기를 지정하거나 루프를 돕니다.
    file_data = sock.recv(1024 * 1024) # 1MB 정도 넉넉히 설정
    
    if file_data == b'No File':
        print("서버에 해당 파일이 존재하지 않습니다.")
    else:
        with open("received_" + fname, 'wb') as f:
            f.write(file_data)
        print(f"파일 수신 완료: received_{fname}")

# TCP는 연결을 끊는 것 자체가 종료 신호이므로 'Bye'를 따로 보낼 필요가 없습니다.
sock.close()