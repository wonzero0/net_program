import requests

url = "API_URL"

params = {
    "serviceKey":"본인키",
    "returnType":"json"
}

res = requests.get(
    url,
    params=params
)

print(res.json())