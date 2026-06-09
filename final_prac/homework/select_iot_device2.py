import socket, time, random, threading

def send_data(conn):
    while True:
        heart = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)
        data = f"Device2: Heartbeat={heart}, Steps={steps}, Cal={cal}"
        conn.send(data.encode())
        time.sleep(5) # 5초 주기

s = socket.socket()
s.bind(('', 2502))
s.listen(5)
print("Device 2 대기 중...")
conn, addr = s.accept()

if conn.recv(1024).decode() == 'Register':
    print("Device 2 등록됨, 데이터 전송 시작")
    threading.Thread(target=send_data, args=(conn,), daemon=True).start()
    while True: time.sleep(1)