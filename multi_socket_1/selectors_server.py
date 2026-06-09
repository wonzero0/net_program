import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()
    print('connected from', addr)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    if not data:
        sel.unregister(conn)
        conn.close()
        return
    print('received data:', data.decode())
    conn.send(data)

sock = socket.socket()
sock.bind(('', 2500))
sock.listen(5)

sel.register(sock, selectors.EVENT_READ, accept)
while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)