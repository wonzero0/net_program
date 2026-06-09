import httpx
import asyncio
import time

async def get_pokemon(client, url):
    rsp = await client.get(url)
    pokemon = rsp.json()
    return pokemon['name']


async def main():
    async with httpx.AsyncClient() as client:
        tasks = []
        for number in range(1, 11):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.create_task(get_pokemon(client, url)))

        original_pokemon = await asyncio.gather(*tasks)

        for pokemon in original_pokemon:
            print(pokemon)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())

    print("--- %s seconds ---" % (time.time() - start_time))