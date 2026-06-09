# [문제 3] 외부 API 연동 및 데이터 처리 (10점)
# OpenWeatherMap API(또는 유사한 날씨 API)를 사용하여 현재 학교 위치의 기온과 습도를 가져오고, 
# 그 결과를 화면에 출력하는 프로그램을 작성하라. (API 키는 환경 변수에서 읽어올 것)

import requests
import os

# API 호출 예시
def get_weather():
    api_key = os.getenv('API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Asan&appid={api_key}"
    response = requests.get(url)
    print(response.json())