# 웹 페이지에서 휴대폰 번호를 추출하는 프로그램을 작성하라.

# 정규표현식 사용 필수

import requests
import re

html = requests.get(
    "https://example.com"
).text

phones = re.findall(
    r'010-\d{4}-\d{4}',
    html
)

for p in phones:
    print(p)