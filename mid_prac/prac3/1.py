# ✅ 1번. 파이썬 문자열 & 슬라이싱 (10점)

# 다음 문자열에 대해 조건을 만족하는 프로그램을 작성하라.

# s = "NetworkProgramming"
# 문제

# A. 문자열을 2번 반복하여 출력
# B. 앞에서 7글자 출력
# C. 뒤에서 11글자 출력
# D. 짝수 인덱스 문자만 출력
# E. 문자열을 역순으로 출력
# F. 뒤에서부터 7글자 출력

# (반복문 사용 금지)

s = "NetworkProgramming"

print(s*2)
print(s[:7])
print(s[-11:])
print(s[::2])
print(s[::-1])
print(s[-7:])