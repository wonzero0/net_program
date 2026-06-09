import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 9999))  

s.send(b'REQ')               
data = s.recv(1024)            

id, temp, hum, seq = struct.unpack('!HBBI', data)

print(id, temp, hum, seq)

s.close()