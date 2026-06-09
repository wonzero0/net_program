import socket

server_addr = ('localhost', 6789)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(b'Hello', server_addr)      # 서버 주소로 Hello 라는 문자열 전송 

data, addr = sock.recvfrom(1024)
if data.decode() == 'Filename':         # 서버가 무슨 파일이 필요할까 라고 물어보면 실행 되는 문구 
    fname = input("받고 싶은 파일 이름을 입력하세요: ")    # 사용자가 받고 싶은 파일명을 직접 키보드로 입력 받음 
    sock.sendto(fname.encode(), server_addr)             # 파일 이름을 바이트 형태로 바꿔서 서버에 전송 
    
    file_data, addr = sock.recvfrom(4096)               # 서버가 보낸 파일의 진짜 내용을 받음 
    
    if file_data == b'No File':                         # 만약 서버가 파일을 못 찾아서 No File 이라는 문자를 받았다면 
        print("서버에 해당 파일이 존재하지 않습니다.")
    else:
        with open("received_" + fname, 'wb') as f:      # 파일 이름 앞에 received_를 붙여서 바이너리 쓰기 모드로 파일 생성 
            f.write(file_data)                          # 서버로부터 받은 file_data를 그 파일 안에 집어넣음 
        print(f"파일 수신 완료: received_{fname}")      
        
        sock.sendto(b'Bye', server_addr)                # 서버에게 잘 받았으니 그만 보내라는 의미로 Bye 신호 전송

sock.close()