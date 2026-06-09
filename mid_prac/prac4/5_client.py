import socket
import struct

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

client.send(b'Hello')

data = client.recv(1024)

id, temp, hum, seq = struct.unpack('!HBBI', data)

print(f"ID:{id}, Temp:{temp}, Hum:{hum}, Seq:{seq}")

client.close()