import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("입력: ")
    client.sendto(msg.encode(), ('localhost', 8888))

    data, _ = client.recvfrom(1024)
    print("서버:", data.decode())