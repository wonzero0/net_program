import httpx
import asyncio

async def fetch_page(client, url):
    response = await client.get(url)
    print(f"URL: {url} | Status Code: {response.status_code}")
    return response.status_code

async def main():
    urls = [
        "https://home.sch.ac.kr/iot/",
        "https://home.sch.ac.kr/aibigdata/"
        ]   
    
    async with httpx.AsyncClient() as client:
        tasks = [fetch_page(client, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print(f"완료된 요청 수: {len(results)}")

if __name__ == "__main__":
    asyncio.run(main())