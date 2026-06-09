from socket import *
import time

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('localhost', 6789))
print("파일 서버 실행 중...")

while True:
    data, addr = s.recvfrom(1024)
    if data.decode() != 'Hello':        # 클라이언트로부터 받은 메세지가 Hello가 아닐 시 위에서부터 다시 시작 
        continue

    s.sendto(b'Filename', addr)         # 클라이언트에게 어떤 파일을 줄건지 물어봄 

    data, addr = s.recvfrom(1024)
    filename = data.decode()            # 받은 데이터를 문자열로 변환하여 filename 변수에 할당 
    print(f"요청 파일: {filename}")     

    try:
        f = open(filename, 'rb')        # filename에 해당하는 파일을 바이너리 읽기 모드로 열어서 통째로 읽어옴 
        content = f.read()
        f.close()

        for attempt in range(3):        # 파일을 보내고 확인 받는 과정을 최대 3번 반복 시도 
            s.sendto(content, addr)     # 실제 파일 데이터를 클라이언트에게 전송 
            print(f"파일 전송 시도 {attempt + 1}회")    # 현재 몇 번째로 파일을 보내고 있는지 화면에 출력 

            s.settimeout(2)             # 2초 동안 대답 없으면 에러 내는 타이머 설정 

            try:
                ack, addr = s.recvfrom(1024)
                if ack.decode() == 'Bye':       # 만약 받은 신호가 Bye 라면 성공적으로 끝난 것이므로 break로 for문 빠져나감
                    print("파일 전송 완료 - 'Bye' 수신")
                    break
            except timeout:
                print(f"타임아웃 - 재전송 시도 {attempt + 1}회")    
                time.sleep(2)   # 2초동안 쉬없다가 다음 전송 시도로 넘어감

        s.settimeout(None)      # 파일 전송이 끝났으니 타이머를 끄고 다시 무한 대기 상태로 돌려놓음 

    except FileNotFoundError:           # 만약 클라이언트가 요청한 파일이 내 컴퓨터에 없을 때 실행 
        s.sendto(b'No File', addr)      # 클라이언트에게 No File이라는 문구 전송 
        print("파일 없음 - 'No File' 전송")

        s.recvfrom(1024)

s.close()