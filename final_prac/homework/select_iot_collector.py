import selectors, socket, time

sel = selectors.DefaultSelector()
f = open("data.txt", "a")

def read(conn, mask):
    try:
        data = conn.recv(1024).decode()
        if data:
            log = f"{time.ctime()}: {data}\n"
            print(log.strip())
            f.write(log)
            f.flush()
    except:
        sel.unregister(conn)
        conn.close()

# 두 디바이스 연결
for port in [2501, 2502]:
    sock = socket.socket()
    sock.connect(('localhost', port))
    sock.send('Register'.encode())
    sel.register(sock, selectors.EVENT_READ, read)

print("데이터 수집기 가동 중 (Ctrl+C로 종료)...")
try:
    while True:
        for key, mask in sel.select():
            key.data(key.fileobj, mask)
except KeyboardInterrupt:
    f.close()
    print("수집 종료 및 파일 저장 완료.")



# ======= selectors 모듈 사용 (저수준 방식)
# import selectors
# import socket
# import time

# sel = selectors.DefaultSelector()

# def send_register(sock):
#     sock.send(b'Register')

# # 서버(디바이스) 주소 설정 (예시)
# devices = [('localhost', 9001), ('localhost', 9002)]
# conns = []

# for addr in devices:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect(addr)
#     sock.setblocking(False)
#     send_register(sock)
#     sel.register(sock, selectors.EVENT_READ)
#     conns.append(sock)

# with open('data.txt', 'a') as f:
#     count = 0
#     while count < 10:
#         events = sel.select()
#         for key, mask in events:
#             sock = key.fileobj
#             data = sock.recv(1024).decode()
#             if data:
#                 timestamp = time.ctime()
#                 log = f"{timestamp}: {data}\n"
#                 print(log.strip())
#                 f.write(log)
#                 count += 1
# sel.close()

# =========== asyncio 모듈 사용 (현대적 방식)
# import asyncio
# import time

# async def collect_data(reader, writer, device_name):
#     writer.write(b'Register')
#     await writer.drain()
    
#     with open('data.txt', 'a') as f:
#         for _ in range(5):  # 디바이스당 5개씩
#             data = await reader.read(100)
#             log = f"{time.ctime()}: {device_name}: {data.decode()}\n"
#             print(log.strip())
#             f.write(log)
#     writer.close()
#     await writer.wait_closed()

# async def main():
#     # 디바이스 1, 2와 동시에 연결
#     conn1 = asyncio.open_connection('localhost', 9001)
#     conn2 = asyncio.open_connection('localhost', 9002)
    
#     r1, w1 = await conn1
#     r2, w2 = await conn2
    
#     await asyncio.gather(
#         collect_data(r1, w1, "Device1"),
#         collect_data(r2, w2, "Device2")
#     )

# asyncio.run(main())