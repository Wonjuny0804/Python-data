"""
실수 1개 입력받아 부분별로 출력하기

실수 1개가 입력된다.
단 입력값은 절대값이 10000을 넘지 않으며, 소수점 이하 자릿수는
최대 6자리까지이고 0이 아닌 숫자로 시작한다.

출력의 경우 첫 번째 줄에 정수 부분을, 두번째 줄에 실수 부분을
출력한다.

"""
#first, second = input().split(".")
#print(first+"\n"+second)

number = float(input())
print(number)
if number < 1:
    print("0\n")
    print(number)
elif number == 1 or number == 0:
    print(number)
else:
    if "." in str(number):
        tmp=str(number).split(".")