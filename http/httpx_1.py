import httpx

# GET 요청
response = httpx.get("https://www.google.com")
print(response.status_code) 
print(response.text)

# POST 요청 (데이터 전송)
data = {"key": "value"}
response = httpx.post("https://httpbin.org/post", data=data)
print(response.json()) 