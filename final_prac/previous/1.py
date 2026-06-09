import http.server
import socketserver

PORT = 8888

class MyHandler(http.server.SimpleHTTPRequestHandler):              # SimpleHTTPRequestHandler 를 상속받음  
    def do_GET(self):                                               # do_GET 메서드 재정의
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            self.end_headers()
            with open('iot.png', 'rb') as f:                        # 접속하면 지정된 iot.png 파일을 바이너리 모드로 전송 
                self.wfile.write(f.read())

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()


# ======= selectors 모듈 사용 =============
# import selectors
# import socket

# sel = selectors.DefaultSelector()

# def accept(sock, mask):
#     conn, addr = sock.accept()
#     conn.setblocking(False)
#     sel.register(conn, selectors.EVENT_READ, read)

# def read(conn, mask):
#     data = conn.recv(1024)
#     if data:
#         # HTTP 응답 헤더와 이미지 데이터 전송
#         with open('iot.png', 'rb') as f:
#             header = b"HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n"
#             conn.sendall(header + f.read())
#     conn.close()
#     sel.unregister(conn)

# server = socket.socket()
# server.bind(('localhost', 8888))
# server.listen(10)
# server.setblocking(False)
# sel.register(server, selectors.EVENT_READ, accept)

# while True:
#     for key, mask in sel.select():
#         callback = key.data
#         callback(key.fileobj, mask)

# ======================= asyncio + httpx 사용 ====================
# import asyncio

# async def handle_client(reader, writer):
#     request = await reader.read(1024)
#     with open('iot.png', 'rb') as f:
#         header = b"HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n"
#         writer.write(header + f.read())
#     await writer.drain()
#     writer.close()

# async def main():
#     server = await asyncio.start_server(handle_client, 'localhost', 8888)
#     async with server:
#         await server.serve_forever()

# asyncio.run(main())