import socket

server_addr = ('localhost', 5050)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_addr)

sock.send('Hello'.encode())  
# 서버에게 Hello 문자열을 바이트 단위로 변환하여 전송 
# -> 서버가 12바이트만 들어있는 완성된 패킷으로 보냈기 때문에 recv(12)가 됨 

data = sock.recv(12)                                # 받는 데이터를 최대 12바이트로 받아들여옴 

sender_id = int.from_bytes(data[0:2], 'big')        # 받은 데이터를 빅엔디언 형태로 받되, 거기서 2바이트는 송신자 id로 확인 
receiver_id = int.from_bytes(data[2:4], 'big') 
lumi = int.from_bytes(data[4:5], 'big')       
humi = int.from_bytes(data[5:6], 'big')      
temp = int.from_bytes(data[6:7], 'big')       
air = int.from_bytes(data[7:8], 'big')        
seq = int.from_bytes(data[8:12], 'big')     

# sender_id, receiver_id, lumi, humi, temp, air, seq = struct.unpack('!HHBBBBI', data)

print(f"Sender:{sender_id}, Receiver:{receiver_id}, Lumi:{lumi}, Humi:{humi}, Temp:{temp}, Air:{air}, Seq:{seq}")

sock.close()