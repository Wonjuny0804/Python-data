"""
숫자의 총합 구하기
사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을
구하는 프로그램을 작성하시오. 
(단 숫자는 콤마로 입력된다.)
"""
all = input().split(",")
total = 0
for thing in all:
    total += int(thing)
print(total)