# 4. [신뢰성 있는 UDP 설계] (20점)
# 이 로직은 보통 '멈추고 기다리기(Stop-and-Wait)' 방식이라고 부릅니다. 핵심은 타임아웃과 재전송입니다.

# 1. 필수 구성 요소 (이건 꼭 들어가야 해요!)
# s.settimeout(2.0): 서버가 죽었거나 패킷이 사라졌을 때 무한정 기다리지 않게 하는 안전장치입니다.

# for 또는 while 루프: 최대 3회라는 재전송 횟수를 관리합니다.

# try - except socket.timeout: 타임아웃 에러가 발생했을 때 재전송 로직으로 넘겨주는 통로입니다.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(2.0)                 # UDP 손실 복구 처리를 위해 타임아웃 처리 

addr = ('localhost', 9999)
msg = 'Hello, server'

for attempt in range(3):                                # 최대 3회 재전송 횟수 
    try:
        s.sendto(msg.encode(), addr)                    # msg 데이터를 인코딩하여 addr로 전송 
        print(f"메시지 전송 ({attempt + 1}회차)")        

        data, server = s.recvfrom(1024)                 # 서버로부터 받은 데이터를 받아 data라는 변수에 저장 

        print("서버 응답 수신 완료: ", data.decode())    # 받은 데이터를 디코딩하여 출력
        break

    except socket.timeout:                              # 타임아웃 발생 시
        if attempt < 2:                                 # 최대 3번 재전송 횟수 
            print(f"타임아웃 발생! 재전송 중... (남은 기회: {2 - attempt}번)")
        else:
            print("최종 전송 실패: 서버가 응답하지 않습니다.")

s.close()