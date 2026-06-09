# import re
# import requests

# url = "https://labs.sch.ac.kr/department/iot/01.php#department-professors"
# response = requests.get(url)
# emails = re.findall(r'[a-zA-Z0-9._%+-]+@sch\.ac\.kr', response.text)

# for email in set(emails): # 중복 제거
#     print(email)


import re
import requests

# 1. URL 설정
url = "https://labs.sch.ac.kr/department/iot/01.php#department-professorS"

# 2. 헤더 추가 (웹 서버가 파이썬 코드를 봇으로 차단하는 것을 방지)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    # 3. 데이터 요청
    response = requests.get(url, headers=headers)
    response.raise_for_status() # 오류 발생 시 예외 처리

    # 4. 정규표현식으로 이메일 추출
    # 학과 교수님들 이메일 패턴: 아이디@sch.ac.kr
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@sch\.ac\.kr', response.text)

    # 5. 중복 제거 및 출력
    if emails:
        for email in sorted(set(emails)):
            print(email)
    else:
        print("추출된 이메일이 없습니다. 웹 페이지 구조를 확인하세요.")

except Exception as e:
    print(f"오류 발생: {e}")