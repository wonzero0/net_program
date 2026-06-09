import asyncio

async def coro_a():
    print("I am coro_a(). Hi!")

async def coro_b():
    print("I am coro_b(). I sure hope no one hogs the event loop...")

async def main():
    task_b = asyncio.create_task(coro_b())          # coro_b() 가 이벤트 루프에 등록되면, 해당 줄은 대기(실행X) 후 다음 코드로 넘어감
    num_repeats = 3
    for _ in range(num_repeats):
        await coro_a()
    await task_b

asyncio.run(main())