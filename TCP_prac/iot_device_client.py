from socket import * 
import time       

f = open('data.txt', 'a')                       # 데이터를 저장할 파일 열기, a는 이어쓰기 라는 뜻

while True: 
    menu = input("접속 디바이스(1/2/quit): ")    # 사용자로부터 입력 받기 
    
    if menu == 'quit':                          # quit 라는 입력이 들어온다면 
        for p in [5555, 6666]:                  # 5555, 6666 서버 모두에게 연결 끊기라는 신호 전달 
            s = socket(AF_INET, SOCK_STREAM)
            s.connect(('localhost', p))     
            s.send(b'quit')                  
            s.close()                        
        break

    if menu == '1' or menu == '2':              # 1 또는 2 입력이 들어온다면 
        target_port = 5555 if menu == '1' else 6666     # 해당 포트 번호 확인 
        s = socket(AF_INET, SOCK_STREAM)        
        s.connect(('localhost', target_port)) 
        s.send(b'Request')                              # Request라는 문구를 보냄으로써 데이터 요청
        
        data = s.recv(1024).decode()                    # 서버가 보낸 데이터를 문자열로 변환해서 받기
        msg = f"{time.ctime()}: Device{menu}: {data}\n"     # 시간과 내용을 합쳐셔서 출력 
        
        f.write(msg)                                # 파일에 기록 
        f.flush()                                   # 파일에 즉시 작성 
        print(msg)                                  # 터미널에 출력 
        s.close()                                   # 요청은 끊되, 서버는 아직 살아있음 

f.close() 