import socket

port = 9999 
# 1. SOCK_STREAM (TCP) 사용
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen(5)

mailboxes = {} 

print("TCP Message Server is running...")

while True:
    # 2. 연결 수락
    conn, addr = s.accept()
    print(f"Connected by {addr}")

    while True:
        try:
            data = conn.recv(1024)
            if not data: break # 연결이 끊기면 중단
            
            # TCP는 데이터가 확실히 오기 때문에 손실 확률(random) 로직은 보통 뺍니다.
            msg = data.decode().strip()
            
            if msg.lower() == 'quit':
                conn.sendall(b'ack')
                break
                
            parts = msg.split(' ', 2)
            command = parts[0].lower()

            if command == 'send' and len(parts) >= 3:
                mboxID, content = parts[1], parts[2]
                if mboxID not in mailboxes: mailboxes[mboxID] = []
                mailboxes[mboxID].append(content)
                conn.sendall(b'OK')
                print(f"[{mboxID}] 저장 완료: {content}")

            elif command == 'receive' and len(parts) >= 2:
                mboxID = parts[1]
                if mboxID in mailboxes and mailboxes[mboxID]:
                    response = mailboxes[mboxID].pop(0)
                else:
                    response = "No messages"
                conn.sendall(response.encode())
                print(f"[{mboxID}] 전송: {response}")

            else:
                conn.sendall(b"Invalid Command")
        except:
            break
            
    conn.close() # 통신 종료 후 소켓 닫기