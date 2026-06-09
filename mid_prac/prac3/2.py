# ✅ 2번. Git (branch / merge / 충돌) (15점)

# 다음 상황을 보고 물음에 답하라.

# 상황
# main 브랜치에서 file.txt 존재
# branch feature 생성
# 두 브랜치에서 같은 줄 수정 후 merge 수행
# 문제

# A. branch 생성 및 이동 명령어 작성
# B. feature 브랜치를 main에 merge하는 명령어 작성
# C. 충돌 발생 이유 설명
# D. 충돌 해결 방법 설명



# ✅ 정답

# A.

# git checkout -b feature

# B.

# git checkout main
# git merge feature

# C.
# 같은 파일의 **같은 위치(line)**를 두 브랜치에서 수정했기 때문에 충돌 발생

# D.

# 충돌 파일 열기
# <<<<<<<, =======, >>>>>>> 부분 수정
# 원하는 내용으로 정리
# 이후:
# git add file.txt
# git commit -m "resolve conflict"
# 💡 해설
# Git은 줄 단위 비교
# 다른 위치 수정 → 자동 merge
# 같은 위치 수정 → ❌ 충돌 발생

# 👉 강의 슬라이드 그대로 출제되는 핵심 문제