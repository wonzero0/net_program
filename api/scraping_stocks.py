import requests
import re
url = 'https://finance.naver.com/item/main.nhn?code=005930'
rsp = requests.get(url)
html = rsp.text                 # 받아온 페이지 전체 내용을 문자열 형태로 저장 
stock_results = re.findall(r'<dl class="blind">([\s\S]+?)<\/dl>', html)  
# <dl class="blind">: 웹페이지 소스에서 주식 정보가 담긴 dl 태그를 찾습니다.
# ([\s\S]+?): 그 안의 모든 내용(줄바꿈 포함)을 다 가져오라는 뜻입니다.

samsung_stock = stock_results[0] 
# dl class="blind"로 시작하는 영역이 여러 개 있는데, 그중 가장 처음에 나오는(0번 인덱스) 유용한 정보가 담긴 덩어리만 따로 변수에 저장

info_list = re.findall(r'<dd>([\s\S]+?)<\/dd>', samsung_stock)
# samsung_stock 영역 내부에서, 실제 데이터가 들어있는 <dd>와 </dd> 사이의 글자들만 골라내어 리스트로 만듭니다.

for info in info_list:
    print(info)