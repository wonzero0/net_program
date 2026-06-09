import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b'REQ', ('localhost', 9999))

data, _ = s.recvfrom(1024)

temp, hum = struct.unpack('!hh', data)

print(temp, hum)