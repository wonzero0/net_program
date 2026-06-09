import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# client_id와 client_secret을 여기에 입력하세요
client_id = "5EmDB_tq_sMvgz1DV0Wl"
client_secret = "lqyM6p54Ep"

rows = 3
cols = 3
query = "고양이" 
display_count = rows * cols 
url = "https://openapi.naver.com/v1/search/image"
images = []

# 이미지 9개를 채울 때까지 반복
while len(images) < 9:
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    params = {
        "query": query,
        "display": 10, # 한 번에 10개씩 가져와서 필요한 만큼 사용
        "start": len(images) + 1, # 이전까지 가져온 개수 다음부터 시작
        "sort": "sim"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        for item in data['items']:
            if len(images) >= 9:
                break
            image_url = item['link']
            try:
                image_response = requests.get(image_url, timeout=5)
                image_response.raise_for_status()
                img = Image.open(BytesIO(image_response.content))
                images.append(img)
            except Exception as e:
                print(f"이미지 처리 실패: {e}")
    else:
        print(f"Error Code: {response.status_code}")
        print(response.text)
        break

# 결과 출력
fig, axes = plt.subplots(rows, cols, figsize=(8, 8))
axes = axes.ravel() 

for i in range(len(images)):
    axes[i].imshow(images[i])
    axes[i].axis('off')
    axes[i].set_title(f"#{i+1}", fontsize=10)

plt.tight_layout()
plt.show()