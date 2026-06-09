import socket

server_addr = ('localhost', 9999)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("측정 정보 선택 (1:온도, 2:습도, 3:조도, q:종료): ")
    
    if msg == 'q': break
    if msg not in ['1', '2', '3']: continue         # 입력 받은 값이 1, 2, 3 중에 없으면 계속 받기 

    sock.sendto(msg.encode(), server_addr)          # 위에서 지정한 서버의 주소로 msg 값을 바이트로 변환하여 서버에게 전송 

    data, addr = sock.recvfrom(1024)
    
    temp = int.from_bytes(data[0:2], 'big')         # 서버로부터 받은 데이터를 슬라이싱 하여 2바이트씩 잘라냄 
    humid = int.from_bytes(data[2:4], 'big')
    lumi = int.from_bytes(data[4:6], 'big')

    # temp, humid, lumi = struct.unpack('!HHH', data) -> strcut로 바꾸면 이렇게 됨

    print(f"Temp={temp}, Humid={humid}, Lumi={lumi}")

sock.close()



# ======================================================
# 만약 UDP 손실 복구 코드를 추가한다면 
# ... (앞부분 동일) ...
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.settimeout(2.0)  # 1. 타임아웃 설정 (2초 동안 대답 없으면 에러 발생)

# while True:
#     msg = input("측정 정보 선택 (1:온도, 2:습도, 3:조도, q:종료): ")
#     if msg == 'q': break
#     if msg not in ['1', '2', '3']: continue 

#     retransmit_count = 0  # 재전송 횟수 체크
#     while retransmit_count < 3:  # 최대 3번까지 다시 시도
#         try:
#             sock.sendto(msg.encode(), server_addr)
#             data, addr = sock.recvfrom(1024) # 대답 기다리기
            
#             # 대답을 잘 받았으면 데이터 처리 후 탈출!
#             temp, humid, lumi = struct.unpack('!HHH', data)
#             print(f"Temp={temp}, Humid={humid}, Lumi={lumi}")
#             break 

#         except socket.timeout: # 2초 동안 응답이 없으면 이쪽으로 넘어옴
#             retransmit_count += 1
#             print(f"패킷 손실 감지! 재전송 중... ({retransmit_count}/3)")
    
#     if retransmit_count == 3:
#         print("서버 연결 실패: 네트워크 상태를 확인하세요.")

# sock.close()