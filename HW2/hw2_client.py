import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

name = "wonyoung Yeom"
sock.send(name.encode())
 
id_data = sock.recv(4)
student_id = int.from_bytes(id_data, 'big')
print(student_id)

sock.close()





# ============ struct 구조체 사용 ======
# import socket
# import struct # 1. struct 모듈 임포트

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# addr = ('localhost', 9000)
# sock.connect(addr)

# # Hello 메시지 수신 및 출력
# msg = sock.recv(1024)
# print(msg.decode())

# # 이름 전송
# name = "wonyoung Yeom"
# sock.send(name.encode())

# # 학번 데이터 수신 (4바이트)
# id_data = sock.recv(4)

# # 2. int.from_bytes 대신 struct.unpack 사용
# # '!I'의 의미: ! (네트워크/빅엔디언), I (4바이트 정수)
# # unpack은 항상 '튜플()' 형태로 반환하므로 뒤에 [0]을 붙여 첫 번째 값을 꺼냅니다.
# student_id = struct.unpack('!I', id_data)[0]
# print(student_id)

# sock.close()