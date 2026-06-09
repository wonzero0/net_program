from socket import *

port = 9999
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(5)

mailboxes = {}

print("TCP Message Server is running...")

while True:
    conn, addr = s.accept()
    print(f"Connected by {addr}")

    try:
        while True:
            data = conn.recv(1024)
            if not data: break 
            
            msg = data.decode().strip()
            
            if msg.lower() == 'quit':
                print(f"Quit requested by {addr}.")
                break 
                
            parts = msg.split(' ', 2)
            command = parts[0].lower()

            if command == 'send' and len(parts) >= 3:
                mboxID = parts[1]
                content = parts[2]

                if mboxID not in mailboxes:
                    mailboxes[mboxID] = []
                mailboxes[mboxID].append(content)
                
                conn.send(b'OK') 
                print(f"[{mboxID}]에 메시지 저장 완료: {content}")

            elif command == 'receive' and len(parts) >= 2:
                mboxID = parts[1]
                
                if mboxID in mailboxes and mailboxes[mboxID]:
                    response = mailboxes[mboxID].pop(0)
                else:
                    response = "No messages"
                    
                conn.send(response.encode())
                print(f"[{mboxID}]에서 메시지 전송: {response}")

            else:
                conn.send(b"Invalid Command")
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close() 
        print(f"Connection with {addr} closed.")

    s.close()