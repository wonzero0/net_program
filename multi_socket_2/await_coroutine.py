import asyncio, time

async def add(a, b):
    print('In add() func')
    await asyncio.sleep(1)                  # await 사용 시 해당 작업이 완전히 끝날 때까지 다음 줄로 넘어가지 않음 -> 비동기 처리 X, 순차적 실행
    print(a+b)

async def mul(a, b):
    print('In mul() func')
    await asyncio.sleep(2)
    print(a * b)

async def main():
    print(f"started at {time.strftime('%X')}")
    await add(1, 2)
    await mul(3, 4)
    print(f"finished at {time.strftime('%X')}"
)
    
asyncio.run(main())