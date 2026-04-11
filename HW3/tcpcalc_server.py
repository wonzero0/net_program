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
            
            msg = data.decode().strip()
            if msg.lower() == 'q':
                print("Client requested to close.")
                break

            parts = re.findall(r'\d+|[+\-*/]', msg)
            
            if len(parts) == 3:
                num1 = int(parts[0])
                op = parts[1]
                num2 = int(parts[2])

                if op == '+': result = num1 + num2
                elif op == '-': result = num1 - num2
                elif op == '*': result = num1 * num2
                elif op == '/': 
                    result = round(num1 / num2, 1) if num2 != 0 else "Error(DivByZero)"
                
                if isinstance(result, (int, float)):
                    response = f"{float(result):.1f}"
                else:
                    response = str(result)
            else:
                response = "Invalid Input"

            client.send(response.encode())
            
        except Exception as e:
            print(f"Error: {e}")
            break

    client.close()