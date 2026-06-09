import selectors
import socket
import random

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    if data:
        msg = data.decode().strip()
        if msg == '1':
            conn.send(f"Temp={random.randint(0, 40)}".encode())
        elif msg == '2':
            conn.send(f"Humid={random.randint(0, 100)}".encode())
    else:
        sel.unregister(conn)
        conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(10)
server.setblocking(False)
sel.register(server, selectors.EVENT_READ, accept)

print("Selectors 서버 가동 중...")
while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)