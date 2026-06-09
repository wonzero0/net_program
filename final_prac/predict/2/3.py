# 해설

# 기출 2번과 동일한 형태.

# 차이점

# 이미지 대신 HTML 전송
# 반드시 HTTP 응답 메시지 작성

import socket
import select
import random

server = socket.socket()
server.bind(("localhost",9999))
server.listen()

clients = [server]

while True:

    rlist, _, _ = select.select(clients, [], [])

    for sock in rlist:

        if sock == server:

            c, addr = server.accept()
            clients.append(c)

        else:

            data = sock.recv(1024)

            if not data:
                clients.remove(sock)
                sock.close()
                continue

            cmd = data.decode()

            if cmd == "1":
                msg = f"Temp={random.randint(0,40)}"

            elif cmd == "2":
                msg = f"Humid={random.randint(0,100)}"

            elif cmd == "3":
                msg = f"Light={random.randint(0,500)}"

            sock.send(msg.encode())