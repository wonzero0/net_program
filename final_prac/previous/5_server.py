import asyncio
import random

async def handle_client(reader, writer):
    while True:
        data = await reader.read(1024)
        if not data: break
        
        msg = data.decode().strip()
        if msg == '1':
            response = f"Temp={random.randint(0, 40)}"
        elif msg == '2':
            response = f"Humid={random.randint(0, 100)}"
        else:
            continue
            
        writer.write(response.encode())
        await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 9999)
    async with server:
        await server.serve_forever()

print("Asyncio 서버 가동 중...")
asyncio.run(main())