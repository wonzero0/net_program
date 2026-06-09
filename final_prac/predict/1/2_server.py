# [문제 2] 고성능 비동기 TCP 서버 구현 (20점)
# asyncio를 사용하여, 다수의 클라이언트가 동시에 온도 데이터를 전송하는 서버를 작성하라. 
# 각 클라이언트는 주기적으로 [온도값]을 전송하며, 서버는 수신된 데이터를 바탕으로 평균 온도를 계산하여 출력하라. (반드시 asyncio.start_server 사용)

import asyncio

# 공유 리스트: 여러 클라이언트가 보낸 데이터를 한곳에 모음
temperature_data = []

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"클라이언트 접속: {addr}")
    
    try:
        while True:
            # 데이터 수신 대기
            data = await reader.read(100)
            if not data:
                break
            
            # 온도값 파싱 및 데이터 저장
            temp = float(data.decode().strip())
            temperature_data.append(temp)
            
            # 평균 계산 로직
            avg_temp = sum(temperature_data) / len(temperature_data)
            print(f"수신: {temp}°C | 누적 데이터 수: {len(temperature_data)} | 현재 평균: {avg_temp:.2f}°C")
            
            # 클라이언트에게 응답(선택사항)
            writer.write(f"Average: {avg_temp:.2f}".encode())
            await writer.drain()
            
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        print(f"클라이언트 종료: {addr}")
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 9999)
    print("비동기 서버 실행 중... (포트: 9999)")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())