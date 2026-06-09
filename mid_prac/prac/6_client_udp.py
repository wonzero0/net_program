import socket
import struct

server_addr = ('localhost', 5050)
# 1. SOCK_STREAM(TCP)을 SOCK_DGRAM(UDP)으로 변경
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. connect() 과정이 필요 없음! 바로 sendto()로 데이터 전송
sock.sendto('Hello'.encode(), server_addr)

# 3. recv() 대신 recvfrom() 사용
data, addr = sock.recvfrom(12)

# struct.unpack으로 한 번에 데이터 풀기
sender_id, receiver_id, lumi, humi, temp, air, seq = struct.unpack('!HHBBBBI', data)

# ==== struct 사용 X =====
# sender_id   = int.from_bytes(data[0:2], 'big')
# receiver_id = int.from_bytes(data[2:4], 'big')
# lumi        = int.from_bytes(data[4:5], 'big')
# humi        = int.from_bytes(data[5:6], 'big')
# temp        = int.from_bytes(data[6:7], 'big')
# air         = int.from_bytes(data[7:8], 'big')
# seq         = int.from_bytes(data[8:12], 'big')

print(f"Sender:{sender_id}, Receiver:{receiver_id}, Lumi:{lumi}, Humi:{humi}, Temp:{temp}, Air:{air}, Seq:{seq}")

sock.close()