from socket import *

s = socket()
s.bind(('', 80))           
s.listen(10)           

while True:
    c, addr = s.accept()                    

    data = c.recv(1024)            
    msg = data.decode()                       
    
    if not msg:                         
        c.close()
        continue

    req = msg.split('\r\n')                 
    request_line = req[0].split(' ')      
    filename = request_line[1].lstrip('/')  

    print(filename)                     

    try:
        if filename == "index.html":                
            f = open(filename, 'r', encoding='utf-8')
            content = f.read()                                  
            mimeType = 'text/html; charset=utf-8'         
            header = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'       
            c.send(header.encode())                    
            c.send(content.encode())
            f.close()

        
        elif filename in ["iot.png", "favicon.ico"]:
           f = open(filename, 'rb')
           content = f.read()
           mimeType = 'image/png' if 'png' in filename else 'image/x-icon'
           header = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'
           c.send(header.encode())
           c.send(content)
           f.close()

        elif filename.startswith('midterm?name='):                      
            word = filename.split('=')[1]                      
            body = f'Hello, {word}'                              
            header = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n'  
            c.send(header.encode() + body.encode())               

        else:
            raise FileNotFoundError                                

    except FileNotFoundError:
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        body = '<html><head><title>Not Found</title></head><body>Not Found</body></html>'
        c.send(header.encode() + body.encode())

    c.close()