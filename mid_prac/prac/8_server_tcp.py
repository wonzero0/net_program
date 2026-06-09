from socket import *

s = socket(AF_INET, SOCK_STREAM) # 1. SOCK_STREAM (TCP) 사용
s.bind(('localhost', 6789))
s.listen(5)
print("TCP 파일 서버 실행 중...")

while True:
    conn, addr = s.accept() # 2. 클라이언트 연결 수락, conn : 새로운 연결 소켓 
    print(f"연결됨: {addr}")

    try:
        data = conn.recv(1024)
        if data.decode() != 'Hello':
            conn.close()
            continue

        conn.send(b'Filename') # 파일 이름 물어보기

        filename = conn.recv(1024).decode()
        print(f"요청 파일: {filename}")

        # 3. 파일 읽어서 전송
        try:
            with open(filename, 'rb') as f:            # filename 파일을 열어 f라 이름을 지정하고 바이너리 형식으로 읽어 들인다.             
                content = f.read()
            
            # TCP는 한 번에 다 보내도 유실 X
            conn.sendall(content) 
            print("파일 전송 완료")

        except FileNotFoundError:
            conn.send(b'No File')
            print("파일 없음 - 'No File' 전송")

    except Exception as e:
        print(f"에러 발생: {e}")
    
    finally:
        conn.close() # 4. 대화 종료 후 연결 닫기