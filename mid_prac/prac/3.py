from socket import *

s = socket()
s.bind(('', 80))            # 80번 포트를 열고 모든 IP에서 접속 가능하게 설정
s.listen(10)                # 최대 동시 접속 수는 10개로 제한 

while True:
    c, addr = s.accept()                     # 브라우저가 연결 접속 시, 연결 수락하고 c(소켓)와 addr(주소)를 받음

    data = c.recv(1024)                      # 브라우저가 보낸 요청 데이터를 최대 1024바이트로 읽어옴 
    msg = data.decode()                      # 데이터를 문자열로 바꿈 
    
    if not msg:                              # 예외처리 / 만약 들어온 메시지가 없다면 연결을 끊고 다음 손님 기다림 
        c.close()
        continue

    req = msg.split('\r\n')                  # 요청 메세지를 줄 바꿈 기준으로 나눔 
    request_line = req[0].split(' ')         # 첫 줄을 공백으로 나눔 (ex. GET /index.html HTTP/1.1)
    filename = request_line[1].lstrip('/')   # 두 번째 항목인 /index.html에서 앞의 /를 떼어내어 실제 파일 이름인 index.html만 남김

    print(filename)                     

    try:
        if filename == "index.html":                   # HTML 파일을 요청한 경우
            f = open(filename, 'r', encoding='utf-8')  # index.html 파일을 읽기 모드로 오픈 / utf-8 을 지정함으로써 한국어를 읽어들일 때 사용 
            content = f.read()                                  
            mimeType = 'text/html; charset=utf-8'      # 데이터형식이 html, 텍스트는 utf-8이라는 방식으로 암호화 되어있다는 의미     
            header = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'        # 브라우저에게 보낼 규격에 맞는 헤더를 만듦
            c.send(header.encode())                             # 헤더와 파일 내용을 바이트 형태로 변환하여 순서대로 전송 
            c.send(content.encode())
            f.close()

        # # 이미지 파일을 요청한 경우
        # elif filename in ["iot.png", "favicon.ico"]:
        #    f = open(filename, 'rb')
        #    content = f.read()
        #    mimeType = 'image/png' if 'png' in filename else 'image/x-icon'
        #    header = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'
        #    c.send(header.encode())
        #    c.send(content)
        #    f.close()

        elif filename.startswith('exam?q='):                        # 쿼리 데이터 주소가 exam?q= 로 시작하면 
            word = filename.split('=')[1]                           # = 뒷부분의 단어 추출 
            body = f'Hello, {word}'                                 # 인사말을 본문으로 작성 
            header = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n'  
            c.send(header.encode() + body.encode())                 # 헤더와 바디를 바이트 형태로 바꿔서 전송 

        else:
            raise FileNotFoundError                                 # 일부러 에러를 발생, 아래의 except 문으로 넘김

    except FileNotFoundError:
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        body = '<html><head><title>Not Found</title></head><body>Not Found</body></html>'
        c.send(header.encode() + body.encode())

    c.close()