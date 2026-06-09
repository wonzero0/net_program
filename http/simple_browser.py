import requests

url = 'http://localhost:8000'
rsp = requests.get(url)
print(rsp.status_code)
print(rsp.headers)
print(rsp.text)