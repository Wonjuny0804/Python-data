"""
한 줄 구구단
사용자로부터 2~9의 숫자 중 하나를 입력받아 해당 숫자의 구구단을 한 줄로
출력하는 프로그램을 작성하시오. 
"""
number = int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))
print(list(map(lambda x: x * number, range(1,10))))