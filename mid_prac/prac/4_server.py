import socket
import random

host = 'localhost'
port = 9999                         # 포트 번호 9999로 지정 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

print(f"IoT 서버 시작... ({host}:{port})")

while True:
    data, addr = sock.recvfrom(1024)
    request = data.decode()             # 데이터를 문자열로 변환

    temp, humid, lumi = 0, 0, 0

    if request == '1':                  # 들어온 데이터가 1일떄 
        temp = random.randint(1, 50)    
    elif request == '2':
        humid = random.randint(1, 100)
    elif request == '3':
        lumi = random.randint(1, 150)

    t_bytes = temp.to_bytes(2, 'big')       # 컴퓨터는 숫자 20 등을 그대로 보내지 못하기 때문에 2바이트 크기의 상자에 넣어서 전송 
    h_bytes = humid.to_bytes(2, 'big')      # 중요한 숫자부터 앞상자에 넣으라는 의미로 빅엔디언 사용
    l_bytes = lumi.to_bytes(2, 'big')

# response = struct.pack('!HHH', temp, humid, lumi)   -> strcut로 변환한다면 이렇게 됨

    response = t_bytes + h_bytes + l_bytes  # 온도, 습도, 조도 각각 2바이트를 순서대로 붙여서 총 6바이트짜리 꾸러미를 만듦
    sock.sendto(response, addr)             # 요청한 사람의 주소로 전송 
    
    print(f"전송 데이터: Temp={temp}, Humid={humid}, Lumi={lumi}")