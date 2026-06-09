import socket
import random
import struct

port = 5050
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', port))
sock.listen(1)

print(f"TCP IoT 서버 시작... (Port: {port})")

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    
    if data.decode() == 'Hello':                    # 클라이언트가 보낸 데이터가 Hello 라는 문자열이 맞다면 
    
        lumi = random.randint(1, 100)          
        humi = random.randint(1, 100)        
        temp = random.randint(1, 100)         
        air = random.randint(1, 100)         
        c_add = data[1]
        data = random.randint(1, 10)  
        len = data
        msg_len = lumi + humi + temp + air + c_add + data + len


        packet = struct.pack('!HHHBBIs', msg_len, lumi, humi, temp, air, c_add, data) 
        conn.send(packet)       
        print(f"데이터 전송 완료")
    
    conn.close()