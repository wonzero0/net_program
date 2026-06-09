import socket
import random

port = 9999                     
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', port))

mailboxes = {}                               # 메세지를 저장할 딕셔너리 생성 

print("UDP Message Server is running...")

while True:
    data, addr = s.recvfrom(1024)
  
    if random.random() <= 0.25:             # 25% 확률로 데이터 손실 발생 
        print(f"!!! 데이터 손실 발생 : {data.decode()} !!!")        # 서버 화면에 데이터 손실 발생 화면 출력, 단 받은 데이터는 문자열로 변환 
        continue 

    msg = data.decode().strip()             # 받은 데이터를 문자열로 변환하되, 문자열의 양쪽 끝에 있는 쓸데없는 공백이나 줄 바꿈 문자 제거
    
    if msg.lower() == 'quit':               # 받은 msg 데이터를 무조건 소문자로 바꾼 값이 quit 일 때 
        s.sendto(b'ack', addr)              # 종료하기 전, 클라이언트 측에 이미 바이트 단위인 ack 전송
        break
        
    parts = msg.split(' ', 2)               # 클라이언트가 보낸 문장을 공백 기준으로 최대 3개로 쪼갬 
    command = parts[0].lower()              # 첫번째 단어를 소문자로 바꿔서 저장 

    if command == 'send' and len(parts) >= 3:       # 명령어가 send이고 쪼개진 단어가 3개 이상이라면 
        mboxID, content = parts[1], parts[2]        # ID 와 content를 각각 지정 
        if mboxID not in mailboxes: mailboxes[mboxID] = []  # 만약 처음 만들어지는 사물함 ID라면 빈 리스트를 새로 만듦 
        mailboxes[mboxID].append(content)           # 해당 사물함 리스트의 맨 뒤에 메세지 내용 추가 
        s.sendto(b'OK', addr)                       # 클라이언트에게 저장 했다는 의미로 OK 전송 
    
        print(f"[{mboxID}] 저장 완료: {content}")

    elif command == 'receive' and len(parts) >= 2:      # 명령어가 receive이고 쪼개진 단어가 2개 이상이라면 
        mboxID = parts[1]                       
        if mboxID in mailboxes and mailboxes[mboxID]:
            response = mailboxes[mboxID].pop(0)         # 내용 빼내옴 
        else:
            response = "No messages"
        s.sendto(response.encode(), addr)

        print(f"[{mboxID}] 전송: {response}")

    else:
        s.sendto(b"Invalid Command", addr)              # 잘못된 명령어가 들어왔을 때 잘못 됐다고 알려주는 메세지를 클라이언트에 전달 

s.close()