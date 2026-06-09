# 웹 브라우저에서 http://localhost:8888/ 접속 시 현재 시간을 출력하는 웹 서버 프로그램을 작성하라.
# http.server 모듈 사용
# HTML 형태로 출력


from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        now = datetime.now()

        html = f"""
        <html>
        <body>
        <h1>{now}</h1>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(html.encode())

server = HTTPServer(("localhost",8888), Handler)
server.serve_forever()
