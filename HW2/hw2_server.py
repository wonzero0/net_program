import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())

    name_data = client.recv(1024)
    print(name_data.decode())

    student_id = 20231312
    client.send(student_id.to_bytes(4, 'big'))

    client.close()




# ========= struct 구조체 사용하고 싶을 때 ===========
# import socket
# import struct # 1. struct 모듈 임포트 필수!

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('', 9000))
# s.listen(2)

# while True:
#     client, addr = s.accept()
#     print('Connection from ', addr)
#     client.send(b'Hello ' + addr[0].encode())

#     name_data = client.recv(1024)
#     print(name_data.decode())

#     student_id = 20231312
    
#     # 2. to_bytes 대신 struct.pack 사용
#     # '!I'의 의미: ! (네트워크/빅엔디언), I (4바이트 정수)
#     packet = struct.pack('!I', student_id)
#     client.send(packet)

#     client.close()

