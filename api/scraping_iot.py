import re
import requests

url = 'https://home.sch.ac.kr/iot'
rsp = requests.get(url)
html = rsp.text
results = re.findall(r'<p><span>관심분야</span><br>([\d\D]+?)</p>', html)
# 웹페이지에서 '관심분야'라는 제목 바로 다음 지점을 찾음
# [\d\D]+? : \d\D는 "숫자든 문자든 모든 글자(줄바꿈 포함)"를 의미하며, +?는 "그 내용을 짧게(최소한으로) 찾음
# () : 그 사이의 내용만 가져옴 

for id, info in enumerate(results):
    print(id+1, info)

