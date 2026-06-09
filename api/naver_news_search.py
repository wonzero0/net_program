import requests
import json

client_id = "5EmDB_tq_sMvgz1DV0Wl"
client_secret = "wIBnHTrql8"

display_count = 5

url = "https://openapi.naver.com/v1/search/news.json"

headers = {
    "X-Naver-Client-ID" : client_id,
    "X-Naver-Client-Secret" : client_secret
}

params = {
    "query" : "헤드라인",
    "display" : display_count,
    "sort" : "date"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

print(f"\n최신 헤드라인 뉴스 {display_count}개: \n")
for i, item in enumerate(data['items']):
    print(f"{i+1}. {item['title'].replace('<b>', '').replace('</b>', '')} - {item['link']}")




# =========================httpx 버전==============
# import httpx
# import json

# # 아이디와 시크릿키는 실제 값을 넣어주세요
# client_id = "YOUR_CLIENT_ID"
# client_secret = "YOUR_CLIENT_SECRET"

# display_count = 5
# url = "https://openapi.naver.com/v1/search/news.json"

# headers = {
#     "X-Naver-Client-ID" : client_id,
#     "X-Naver-Client-Secret" : client_secret
# }

# params = {
#     "query" : "헤드라인",
#     "display" : display_count,
#     "sort" : "date"
# }

# # requests 대신 httpx를 사용합니다
# response = httpx.get(url, headers=headers, params=params)

# # httpx는 .json() 메서드를 통해 바로 파이썬 딕셔너리로 변환합니다
# data = response.json()

# print(f"\n최신 헤드라인 뉴스 {display_count}개: \n")
# for i, item in enumerate(data['items']):
#     # HTML 태그 제거
#     title = item['title'].replace('<b>', '').replace('</b>', '')
#     print(f"{i+1}. {title} - {item['link']}")

#==========비동기 httpx============
# import httpx
# import asyncio

# async def fetch_news():
#     client_id = "YOUR_CLIENT_ID"
#     client_secret = "YOUR_CLIENT_SECRET"
    
#     url = "https://openapi.naver.com/v1/search/news.json"
#     headers = {
#         "X-Naver-Client-ID": client_id,
#         "X-Naver-Client-Secret": client_secret
#     }
#     params = {
#         "query": "헤드라인",
#         "display": 5,
#         "sort": "date"
#     }

#     # 비동기 클라이언트를 사용하여 요청 보냄
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=headers, params=params)
#         data = response.json()
        
#         print(f"\n최신 헤드라인 뉴스 5개 (비동기): \n")
#         for i, item in enumerate(data['items']):
#             title = item['title'].replace('<b>', '').replace('</b>', '')
#             print(f"{i+1}. {title} - {item['link']}")

# if __name__ == "__main__":
#     # 비동기 함수 실행
#     asyncio.run(fetch_news())