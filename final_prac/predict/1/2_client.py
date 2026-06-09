import asyncio
import random

async def send_temp_data():
    # 서버에 접속
    reader, writer = await asyncio.open_connection('127.0.0.1', 9999)
    print("서버에 연결되었습니다.")
    
    try:
        while True:
            # 랜덤 온도 생성 (0~40)
            temp = random.randint(0, 40)
            message = str(temp)
            
            # 서버로 전송
            writer.write(message.encode())
            await writer.drain()
            print(f"전송 완료: {temp}°C")
            
            # 서버로부터의 응답 수신 대기 (필요 시)
            response = await reader.read(100)
            print(f"서버 응답: {response.decode()}")
            
            await asyncio.sleep(3) # 3초 간격으로 반복
            
    except Exception as e:
        print(f"연결 종료 또는 에러: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(send_temp_data())