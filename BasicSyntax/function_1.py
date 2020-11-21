"""
함수 1
- 반복되는 코드를 묶음으로 효율적인 코드를 작성하도록 해주는 기능
- 기본 함수
- 파라미터와 아규먼트
- 리턴
- `*args`, `**kwargs`
"""
# 1. 기본 함수
# - 함수의 선언과 호출
point = 88

if point >= 90:
    print("A")
elif point >= 80:
    print("B")
else:
    print("C")

# 함수 선언
def grade(point):
    if point >= 90:
        print("A")
    elif point >= 80:
        print("B")
    else:
        print("C")

a = 1
ls = [1, 2, 3]
grade(88)
grade(78)

"""
2. 파라미터와 아규먼트
- 파라미터 : 함수를 선언할때 호출하는 부분에서 보내주는 데이터를 받는 변수
- 아규먼트 : 함수를 호출할때 함수에 보내주는 데이터

"""
def plus(num1, num2=10, num3=20): # 파라미터 : 디폴트 파라미터
    print(num1 + num2 - num3)

plus(1, 2) # 아규먼트
plus(3, num3=100) # 아규먼트 : 키워드 아규먼트

print(1, 2, end="-")
print(3)

"""
3. Return
- 함수를 실행한 결과를 저장하고 싶을때 사용합니다.
- return
"""
def plus1(num1, num2):
    print(num1 + num2)
    return num1 + num2

result = plus1(1, 2)
print(result)

data1 = "python"
result = data1.upper()
print(result)

data2 = [3, 1, 2]
result = data2.sort()
print(result)

# 함수 선언
def grade2(point):
    if point >= 90:
        return "A"
    elif point >= 80:
        return  "B"
    else:
        return "C"

point = 92
result = grade2(point)
print(result)

if result == "A":
    print("pass")
else:
    print("fail")


# 함수에서 return 코드가 실행되면 무조건 함수의 코드 실행이 종료
def echo(msg):
    if msg == "quit":
        return
    print(msg)

echo("python")
echo("quit")

def calc(num1, num2):
    return num1 + num2, num1 - num2
data1, data2 = calc(1, 2)
print(data1, data2)

data1, data2 = (3, -1)
print(data1, data2)

# 4. *args, **kwargs
# - 함수를 호출할때 아규먼트와 키워드 아규먼트의 갯수를 특정지을수 없을때 사용

def plus2(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
    return sum(args) + sum(list(kwargs.values()))

print(plus2(1, 2, 3, 4, 5, num1=6, num2=7))

def func(num1, num2=10, num3=20):
    return num1 + num2 + num3

data = (1, 2, 3)
func(*data) # func(1, 2, 3)
# func(data) # func([1, 2, 3])

data = {
    "num2": 100,
    "num3": 200,
}
func(1, **data) # func(1, num2=100, num3=200)

data = [1,2,3]
for num in data:
    result = num
print(result)

for num in [1, 2, 3]:
    print(num)

