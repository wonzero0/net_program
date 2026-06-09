# [문제 1] 웹 서비스의 이해 (10점)
# 작년과 동일하게 웹 브라우저에서 http://localhost:8888/ 접속 시 특정 JSON 데이터를 반환하는 REST API 서버를 http.server 모듈을 사용하여 작성하라.
# (데이터 형식: {"status": "success", "device": "IoT_Sensor_01"})

import http.server
import socketserver
import json

class SimpleHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        data = {"status": "success", "device": "IoT_Sensor_01"}
        self.wfile.write(json.dumps(data).encode())

with socketserver.TCPServer(("", 8888), SimpleHandler) as httpd:
    httpd.serve_forever()