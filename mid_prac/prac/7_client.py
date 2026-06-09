import socket

server_addr = ('localhost', 9999)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP Message Client (With Retransmission)")

while True:
    user_input = input('Enter message ("send mboxId msg", "receive mboxId", "quit"): ')
    
    reTx = 0                    # 재전송 횟수를 저장할 변수 선언 
    success = False             # 서버로부터 응답을 받았는지 여부를 체크하기 위한 깃발 

    while reTx <= 2:            # 최초 전송부터 재전송 2회까지, 총 3번 시도하겠다는 의미 
        s.sendto(user_input.encode(), server_addr)      # 사용자가 입력한 문자열을 바이트로 바꿔서 서버 주소로 전송 
        s.settimeout(1.0)       # 서버의 답장을 딱 1초만 기다리겠다는 의미

        try:
            data, addr = s.recvfrom(1024)
            print(f"<- {data.decode()}")        # 서버가 보낸 데이터(답장)를 문자열로 바꿔 출력 
            success = True
            break 
        except socket.timeout:                  # 1초 동안 답장이 안 오면 자동으로 넘어옴 
            reTx += 1                           # 실패했으니 reTx 변수 1 증가 
            if reTx <= 2:
                print(f"타임아웃! 재전송 중... ({reTx}/2)")
    
    if not success:
        print("서버 응답 없음: 전송 실패")

    if user_input.lower() == 'quit':
        break

s.close()