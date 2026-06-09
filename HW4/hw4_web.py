from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    
    if not msg:
        c.close()
        continue

    req = msg.split('\r\n')                         # msg 데이터에서 \r\n을 기준으로 자르고 req 변수에 할당 
    request_line = req[0].split(' ')                # 공백을 기준으로 req[0] 번째 데이터 값  -> ['GET', '/index.html', 'HTTP/1.1']  
    filename = request_line[1].lstrip('/')          # request_line[1]에 해당하는 데이터에 붙은 / 제거 -> index.html

    print(filename) 


    try:
        if filename == "index.html":
            f = open(filename, 'r', encoding='utf-8')       # filename을 읽기모드로 open 하되, 한국어도 가능하게! 
            content = f.read()
            mimeType = 'text/html; charset=utf-8'           # 브라우저에게 한글이 포함된 HTML 이라고 알려줌 
            header = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'       # 헤더 정의
            c.send(header.encode())     # 헤더는 문자열이므로 인코딩해서 전송
            c.send(content.encode())    # 읽어온 HTML 내용도 인코딩해서 전송 
            f.close()

        elif filename in ["iot.png", "favicon.ico"]:    # 이미지 파일 처리 
            f = open(filename, 'rb')                    # 그림 파일은 있는 그대로 일기 -> rb : 바이너리 형태로 읽기
            content = f.read()
            mimeType = 'image/png' if 'png' in filename else 'image/x-icon' # 파일 확장자에 따라 MIME 타입을 자동으로 결정 
            header = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'
            c.send(header.encode())
            c.send(content)         # 이미 bytes상태로 인코딩 없이 전송
            f.close()
            
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        body = '<html><head><title>Not Found</title></head><body>Not Found</body></html>'
        c.send(header.encode() + body.encode())

    c.close()