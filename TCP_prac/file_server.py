from socket import *
import os

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)
print('File server is running...')

while True:
    conn, addr = sock.accept()

    msg =  conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    elif msg != b'Hello':
        print('client: ', addr, msg.decode())
        conn.close()
        continue