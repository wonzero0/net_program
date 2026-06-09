# 현재 성인사진 분류 API 종료되어서 실행 불가 / 코드 참고
import requests

headers = {"Authorization": "2648c2003290ebfd6688db25bd01e182"}
files = {"image": open("iot.png", "rb")}
url = "https://dapi.kakao.com/v2/vision/adult/detect"

resp = requests.post(url, headers=headers, files=files)
print(resp.json())