days = {'January':31, 'February':28, 'March':31, 'April':30,     
        'May':31, 'June':30, 'July':31, 'August':31, 
        'September':30, 'October':31, 'November':30,  
        'December':31} 

print(sorted(days.keys()))  # 딕셔너리 왼쪽에 해당하는 key값들을 알파벳 순서로 정렬



# lambda = 간단한 함수를 한 줄로 표현 
# x = 튜플 하나 (ex. 'January', 31)
# x[1] = 튜플의 투 번째 값 (ex. 31)

# days.items(): 딕셔너리에서 ('January', 31) 처럼 (이름, 숫자) 쌍을 통째로 꺼내옵니다.
# lambda x: x[1]: 여기서 x는 방금 꺼낸 ('January', 31) 한 쌍을 말해요. x[1]은 그중 두 번째인 숫자(31)를 의미하죠. 
# 즉, "숫자를 기준으로 정렬해!"라는 규칙을 정해줌
# sorted(..., key=...): 정해진 규칙(숫자)에 따라 전체 목록을 오름차순으로 정렬합니다.
print(sorted(days.items(), key=lambda x: x[1]))


month = input()


# 입력 받은 값이랑 key 값의 3글자가 동일하면 key의 전체 값을 출력
for key in days:
    if key[:3] == month:        
        print(days[key])