import re
import requests

url = 'http://goo.gl/U7mSQl'
rsp = requests.get(url)
html = rsp.text
results = re.findall(r'[A-Za-z0-9]+\*\*\*', html)

# [A-Za-z0-9]+: 영문자나 숫자가 1개 이상 이어짐.
# \*\*\*: 별표 세 개(***)가 뒤에 붙음.

# [A-Z]: A부터 Z까지 모든 대문자 중 하나
# [a-z]: a부터 z까지 모든 소문자 중 하나
# [0-9]: 0부터 9까지 모든 숫자 중 하나
# + : 한글자 이상 게속 이어지는 것


for id in results:
    print(id)