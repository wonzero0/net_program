# 1번 문제를 멀티스레드 TCP 소켓 서버로 작성하라.

import socket
import threading
from datetime import datetime

def client(sock):

    sock.recv(1024)

    html = f"""
    <html>
    <body>
    <h1>{datetime.now()}</h1>
    </body>
    </html>
    """

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type:text/html\r\n"
        "\r\n"
    ).encode()

    sock.send(response)
    sock.send(html.encode())
    sock.close()

server = socket.socket()
server.bind(("localhost",8888))
server.listen()

while True:
    c, addr = server.accept()

    threading.Thread(
        target=client,
        args=(c,)
    ).start()