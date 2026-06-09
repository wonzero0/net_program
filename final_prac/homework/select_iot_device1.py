import socket, time, random, threading

def send_data(conn):
    while True:
        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)
        data = f"Device1: Temp={temp}, Humid={humid}, Illum={illum}"
        conn.send(data.encode())
        time.sleep(3) # 3초 주기

s = socket.socket()
s.bind(('', 2501))
s.listen(5)
print("Device 1 대기 중...")
conn, addr = s.accept()

if conn.recv(1024).decode() == 'Register':
    print("Device 1 등록됨, 데이터 전송 시작")
    threading.Thread(target=send_data, args=(conn,), daemon=True).start()
    while True: time.sleep(1)