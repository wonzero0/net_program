import socket
import random

port = 3333
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

print("채팅 서버 시작...")

while True:
    sock.settimeout(None)                               # 메시지를 처음 기다릴 때는 시간이 얼마나 걸리든 무한정 기다림
    while True: 
        data, addr = sock.recvfrom(BUFF_SIZE)           # 클라이언트가 보낸 데이터와 주소를 받음

        if random.random() <= 0.5:                      # 50% 확률로 조건문에 걸리게 만듦
            continue                                    # 50% 확률에 걸릴 시 아래 코드를 무시하고 다시 위로 올라감 -> 손실 흉내
        else:
            sock.sendto(b'ack', addr)                   # 잘 받았는 의미로 ack 신호를 상대에게 전송 
            print(f'<- {data.decode()}')                # 받은 메시지를 문자열로 바꿔 화면에 출력
            break   

    msg = input('-> ')
    reTx = 0
    while reTx <= 5:                                    # 재전송 횟수가 5번이 넘지 않을 때까지 반복
        resp = str(reTx) + ' ' + msg                    # 재전송 횟수 + 메시지 형태로 만듦 
        sock.sendto(resp.encode(), addr)        
        sock.settimeout(2)                              # 2초 안에 응답이 오지 않으면 에러를 내도록 함 
        
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
            if data.decode() == 'ack':
                break  
        except socket.timeout:                          # 2초 기다린 후에도 응답이 없으면 재전송 횟수를 +1 하고 다시 루프 돌기
            reTx += 1
            print(f"타임아웃 발생! 재전송 횟수: {reTx}")
            continue

    if reTx > 5:
        print("최대 재전송 횟수를 초과하여 전송에 실패했습니다.")