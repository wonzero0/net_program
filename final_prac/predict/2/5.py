# 3번 서버를 asyncio로 작성하라.

import asyncio
import random

async def handle(reader, writer):

    while True:

        data = await reader.read(1024)

        if not data:
            break

        cmd = data.decode()

        if cmd == "1":
            msg = f"Temp={random.randint(0,40)}"

        elif cmd == "2":
            msg = f"Humid={random.randint(0,100)}"

        writer.write(msg.encode())

        await writer.drain()

    writer.close()

async def main():

    server = await asyncio.start_server(
        handle,
        "localhost",
        9999
    )

    async with server:
        await server.serve_forever()

asyncio.run(main())