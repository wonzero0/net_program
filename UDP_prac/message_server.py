from socket import *

port = 9999
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', port))

# 사물함 저장소 (딕셔너리 활용)
# 구조: {'mboxID': ['message1', 'message2', ...]}
mailboxes = {}

print("UDP Message Server is running...")

while True:

    data, addr = s.recvfrom(1024)
    msg = data.decode().strip()
    

    if msg.lower() == 'quit':
        print(f"Quit requested by {addr}. Server shutting down.")
        break
        
    parts = msg.split(' ', 2) # [명령어, mboxID, 메시지내용] 분리
    command = parts[0].lower()

    if command == 'send' and len(parts) >= 3:
        mboxID = parts[1]
        content = parts[2]

        if mboxID not in mailboxes:
            mailboxes[mboxID] = []
        mailboxes[mboxID].append(content)
        
        s.sendto(b'OK', addr)
        print(f"[{mboxID}]에 메시지 저장 완료: {content}")

    elif command == 'receive' and len(parts) >= 2:
        mboxID = parts[1]
        
        if mboxID in mailboxes and mailboxes[mboxID]:
            response = mailboxes[mboxID].pop(0)
        else:
            response = "No messages"
            
        s.sendto(response.encode(), addr)
        print(f"[{mboxID}]에서 메시지 전송: {response}")

    else:
        s.sendto(b"Invalid Command", addr)

s.close()


# ===========TCP 일 때 =====
# from socket import *

# port = 9999
# # 1. SOCK_STREAM(TCP) 소켓 생성 및 대기
# s = socket(AF_INET, SOCK_STREAM)
# s.bind(('', port))
# s.listen(5)

# # 메시지 저장소 (서버가 켜져 있는 동안 유지됨)
# mailboxes = {}

# print("TCP Message Server is running...")

# while True:
#     # 2. 클라이언트 접속 수락 (전용 통로 conn 생성)
#     conn, addr = s.accept()
#     print(f"Connected by {addr}")

#     try:
#         while True:
#             # 3. 연결된 통로를 통해 데이터 수신
#             data = conn.recv(1024)
#             if not data: break # 데이터가 없으면 클라이언트가 연결을 끊은 것
            
#             msg = data.decode().strip()
            
#             # 'quit' 수신 시 해당 클라이언트와 연결 종료
#             if msg.lower() == 'quit':
#                 print(f"Quit requested by {addr}.")
#                 break 
                
#             parts = msg.split(' ', 2)
#             command = parts[0].lower()

#             if command == 'send' and len(parts) >= 3:
#                 mboxID = parts[1]
#                 content = parts[2]

#                 if mboxID not in mailboxes:
#                     mailboxes[mboxID] = []
#                 mailboxes[mboxID].append(content)
                
#                 conn.send(b'OK') # TCP는 주소 없이 conn.send()
#                 print(f"[{mboxID}]에 메시지 저장 완료: {content}")

#             elif command == 'receive' and len(parts) >= 2:
#                 mboxID = parts[1]
                
#                 if mboxID in mailboxes and mailboxes[mboxID]:
#                     response = mailboxes[mboxID].pop(0) # 가장 먼저 들어온 메시지 꺼내기(FIFO)
#                 else:
#                     response = "No messages"
                    
#                 conn.send(response.encode())
#                 print(f"[{mboxID}]에서 메시지 전송: {response}")

#             else:
#                 conn.send(b"Invalid Command")
                
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         conn.close() # 대화가 끝나면 해당 클라이언트 소켓 닫기
#         print(f"Connection with {addr} closed.")

# # 전체 서버 소켓 닫기 (실제로는 무한루프라 여기까지 도달하진 않음)
# s.close()