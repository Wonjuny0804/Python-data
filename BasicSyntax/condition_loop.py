"""
1. 조건문
- 특정 조건에 따라서 코드를 실행하고자 할때 사용
- if, else, elif
"""
# 조건부분에 : bool 데이터 타입 이외의 데이터 타입이 오면 bool으로 형변환 되어 판단

if False:
    print("python")
    
print("done")

# int : 0을 제외한 나머지 값은 True
print(bool(0), bool(1), bool(-1), bool(100))

num = 0

if num:
    print("python_1")

num = 1

if num:
    print("python_2")

number = 7

if number % 2:
    print("홀수")

# float : 0.0을 제외한 나머지 실수는 True
# str : ""를 제외한 나머지 문자열은 True
# list, tuple, dict : [], (), {}를 제외한 나머지는 True

# 지갑에 돈이 10000원 이상 있으면 택시를 탑니다.
# 2000원 이상, 10000원 미만 있으면 버스를 탑니다.
# 그렇지 않으면 걸어서 집에 갑니다.

money = 12000

if money >= 10000:
    print("택시를 타고 집에 갑니다.")

if money < 10000:
    print("걸어서 집에 갑니다.")

money = 4000

if money >= 10000:
    print("택시를 타고 집에 갑니다.")
elif money >= 5000:
    print("광역버스를 타고 집에 갑니다.")
elif money >= 2000:
    print("일반버스를 타고 집에 갑니다.")
else:
    print("걸어서 집에 갑니다.")



account = 10000
draw_money = int(input("insert draw money : "))

if account >= draw_money:
    account -= draw_money
    print(str(draw_money) + "원이 인출 되었습니다.")
else:
    print("인출이 불가능합니다. " + str(draw_money - account) + " 원의 잔액이 부족합니다.")

print("현재 잔액은 " + str(account) + " 원 입니다.")


# string 데이터 타입의 format 함수
print("현재 잔액은 " + str(account) + " 원 입니다.")
print("현재 잔액은 {} 원 입니다. 인출금액은 {} 입니다.".format(account, draw_money))
print("현재 잔액은 {data1} 원 입니다. 인출금액은 {data2} 입니다.".format(data2=draw_money, data1=account))

"""
#### 삼항연산자
- 간단한 if, else 구문을 한줄의 코드로 표현할수 있는 방법
- (True) if (condition) else (False)
"""

# data 변수에 0이면 "zero" 출력, 아니면 "not zero" 출력

data = 1

if data:
    print("not zero")
else:
    print("zero")

data = 0
result = "not zero" if data else "zero"
print(result)

"""
### 2. 반복문
- 반복되는 코드를 실행할때 사용
- while, for, break, continue
- list comprehention

"""

# while
data = 3

while data: # 조건이 False가 될때까지 구문의 코드를 실행
    
    # 반복되는 코드
    print(data)
    data -= 1

# 학생이 국어:80점, 영어:90점, 수학:100점, while 문을 이용해서 총점과 평균을 출력
# 학생의 점수는 list, dict 표현
# len(), dict.values(), list.pop()

subjects_ls = ["korean", "english", "math"]
points_ls = [80, 90, 100]
points_dict = {"korean": 80, "english": 90, "math": 100}

total, avg = 0, 0
datas = points_ls.copy() # 깊은복사 : 원본데이터를 보존

while datas:
    total += datas.pop()

avg = total / len(points_ls)

print(total, avg)

# 무한루프
# break : 반복문을 중단 시킬때 사용되는 예약어
result = 1
while result:
    
    if result >= 10:
        break
        
    result += 1
    
print(result)

"""
### for
- iterable한 값을 하나씩 꺼내서 variable을 대입시킨후 코드를 interable 변수의 값 갯수 만큼 실행
```
for <variable> in <iterables>:
    <code>
```
"""

# for : continue : 조건부분으로 올라가서 코드가 실행
ls = [0, 1, 2, 3, 4]
for data in ls:
    
    if data % 2: # data가 홀수가 되면 continue를 실행
        continue
        
    # data가 짝수이면 print를 실행
    print(data, end=" ")

# for를 이용하여 코드를 100번 실행
# range 함수
list(range(10))
result = 0
for data in range(10):
    result += data
print(result)

# offset index 개념과 비슷하게 사용
print(list(range(5)), list(range(5, 10)), list(range(10, 0, -2)))

# 0~10 까지 짝수를 더한 총합
result = 0
for number in range(0, 11, 2):
    result += number
print(result)

points_dict = {"korean": 80, "english": 90, "math": 100}
print(list(points_dict.keys()))

print(list(points_dict.items()))

for subject, point in points_dict.items():
    print(subject, point)

print(list(zip(subjects_ls, points_ls)))
# for문에서 iterable 데이터가 tuple로 나오면 여러개의 변수로 받을수 있습니다.
subjects_ls = ["korean", "english", "math"]
points_ls = [80, 90, 100]
for subject, point in zip(subjects_ls, points_ls):
    print(subject, point)

"""
- 구구단 출력 (가로 출력)
    - 이중for문 : for문 안에 for문
    - print : end="\t"
    - string : format 함수 이용
```
2*1=2   3*1=3 ... 9*1=9
...
2*9=18  3*9=27... 9*9=81
```
"""

for num2 in range(1, 10):
    for num1 in range(2, 10):
        print("{}*{}={}".format(num1, num2, num1*num2), end="\t")
    print()


"""
### 3. List Comprehention
- 리스트 데이터를 만들어주는 방법
- for문 보다 빠르게 동작합니다.
"""


# 각각 값에 제곱한 결과 출력
ls = [0, 1, 2, 3]
result = []

for data in ls:
    result.append(data**2)
    
print(result)

result = [data**2 for data in ls]
print(result)

# 리스트 컴프리헨션을써서 홀수와 짝수를 리스트로 출력해주는 코드
# 삼항연산 사용
ls = [0, 1, 2, 3]
# result = ["짝수", "홀수", "짝수", "홀수"]

result = [
    "홀수" if data % 2 else "짝수"
    for data in ls
]
print(result)

# 리스트 컴프리헨션 조건문
ls = range(10)
print([data for data in ls if data % 2])


ls = [1, 2, 3]
print([func for func in dir(ls) if func[:2] != "__" and func[0] == "c"])


