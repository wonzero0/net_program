import socket
import struct

server_addr = ('localhost', 5050)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_addr)

sock.send('Hello'.encode())  

data = sock.recv(2)
msg_len = len(data)

for i in range(len(data)):
    data = sock.recv(2)

msg_len, lumi, humi, temp, air, c_add, data = struct.unpack('!HHHBBIs', data)

print(f"Length: {msg_len}, Lumi: {lumi}, Humi: {humi}, Temp: {temp}, Air: {air}, IP: {c_add}, Variable Data: {data}")

sock.close()
