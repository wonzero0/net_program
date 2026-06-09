from socket import *
import re 

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('TCP Calculator Server is running...')

while True:
    client, addr = s.accept()
    print(f'Connected by {addr}')
    
    while True:
        try:
            data = client.recv(1024)
            if not data: break
            
            msg = data.decode().strip()                     # strip() 은 문자열의 양쪽 끝에 있는 공백, 탭, 줄바꿈 문자를 모두 제거     
            if msg.lower() == 'q':
                print("Client requested to close.")
                break

            parts = re.findall(r'\d+|[+\-*/]', msg)         # | 기준으로 문자열에서 숫자와 연산자만 분리해서 리스트로 만들어주기
            
            if len(parts) == 3:                             # 입력받은 데이터 리스트의 길이가 3이 맞다면
                num1 = int(parts[0])                        # 리스트 0번째 데이터를 정수형으로 변환
                op = parts[1]                               # 1번째 데이터는 그대로 사용 
                num2 = int(parts[2])                        # 2번째 데이터 정수형으로 변환하여 사용 

                if op == '+': result = num1 + num2          # 1번째 데이터가 담겨있는 op가 +일 때 
                elif op == '-': result = num1 - num2
                elif op == '*': result = num1 * num2
                elif op == '/': 
                    result = round(num1 / num2, 1) if num2 != 0 else "Error(DivByZero)"  # 나누는 수가 0이라면 계산 대신 에러라는 문자 출력
                
                if isinstance(result, (int, float)):        # result 변수에 들어있는 값이 정수나 실수인지 확인
                    response = f"{float(result):.1f}"       # float형이라면 무조건 소수점 한 자리로
                else:
                    response = str(result)                  # 결과가 아닌 Error(DiveByZero) 와 같은 문자열이라면 그대로 두기
            else:
                response = "Invalid Input"                  # 리스트의 길이가 3이 아니라면 Invalid Input 이라는 문자

            client.send(response.encode())                  # respone에 담겨있는 데이터를 인코딩하여 클라이언트에 전송

        except Exception as e:                              # 서버 안정성 보장 -> 에러가 발생했을 때 서버 끄지말고, 어떤 에러인지 터미널에 출력
            print(f"Error: {e}")
            break

    client.close()


# =====================UDP 연결일 때==============
# from socket import *
# import re 

# # 1. SOCK_DGRAM으로 설정하여 UDP 소켓 생성
# s = socket(AF_INET, SOCK_DGRAM)
# s.bind(('', 3333))
# print('UDP Calculator Server is running...')

# while True:
#     try:
#         # 2. UDP는 accept() 없이 바로 recvfrom()으로 데이터와 주소를 동시에 받음
#         data, addr = s.recvfrom(1024)
#         msg = data.decode().strip()
        
#         if msg.lower() == 'q':
#             print(f"Client {addr} requested to quit.")
#             continue # UDP는 개별 연결이 없으므로 루프를 계속 돕니다.

#         # 문자열 분석 (기존 로직 동일)
#         parts = re.findall(r'\d+|[+\-*/]', msg)
        
#         if len(parts) == 3:
#             num1 = int(parts[0])
#             op = parts[1]
#             num2 = int(parts[2])

#             if op == '+': result = num1 + num2
#             elif op == '-': result = num1 - num2
#             elif op == '*': result = num1 * num2
#             elif op == '/': 
#                 result = round(num1 / num2, 1) if num2 != 0 else "Error(DivByZero)"
            
#             if isinstance(result, (int, float)):
#                 response = f"{float(result):.1f}"
#             else:
#                 response = str(result)
#         else:
#             response = "Invalid Input"

#         # 3. 답장을 보낼 때는 반드시 받은 주소(addr)를 적어서 sendto() 사용
#         s.sendto(response.encode(), addr)
#         print(f"Processed: {msg} -> {response} (to {addr})")

#     except Exception as e:
#         print(f"Error: {e}")
#         # UDP는 에러가 나도 소켓이 닫히지 않게 계속 유지하는 것이 좋습니다.

# s.close()