# 문장을 입력받아서 문법에 맞도록 결과를 출력하는 코드를 작성
# 마지막 문자는 . 이 있을수도 있고 없을수도 있습니다.
# 논리적인 문제해결 순서 -> 코드로 변경
# str.upper(), str.lower(),, offset index [], str.__add__(문자열 덧셈)

# python IS the best Language / python IS the best Language.
# Python is the best language.

# 1. 문자열 입력 받기
sentence = input("input sentence :")

# 2. 모두 소문자로 변경
result = sentence.lower()

# 3. 가장 앞글자를 대문자로 변경
result = result[0].upper() + result[1:]

# 4. 마지막 문자가 . 인지확인해서 .이 아니면 .를 추가
if result[-1] != ".":
    result += "."

result

# 6자리의 로또번호를 생성하는 코드를 작성하세요.
# 6자리의 번호는 중복이 X
# 문자열, 숫자, 리스트
# while, not in, in, list.append(), break, len(), list.sort()
# 문제가 조금 복잡하면 간단한 기능부터 구현하고 업데이트를 하는 방법으로 해결
# 랜덤한숫자 6개 출력 -> 숫자가 중복되지 않는 코드를 추가

import random

# random.randint(1, 45)

lotto = []

# 랜덤한 숫자 6개를 while문을 사용해서 작성
while True:
    
    number = random.randint(1, 45)
    
    # 숫자를 추가할때 lotto 리스트에 중복되는 숫자가 없으면 추가
    if number not in lotto:
        lotto.append(number)
    
    if len(lotto) >= 6:
        lotto.sort()
        break

print(lotto)


"""
- 함수
    - 중복되는 코드를 묶어서 효율적으로 코드를 작성하기 위해 사용
    - 기본함수 : 선언(def), 호출(func_name())
    - argument, parameter, keyword argment, default parameter
    - return 
    - `*args`, `**kwargs`

"""

# 함수 2
"""
- docstring
- scope
- inner function
- lambda function
- map, filter, reduce
- decorlator
"""

# 1. Docstring
# - 함수의 설명을 작성
def echo(msg):
    """
    echo func return its input agument
    The operation is:
        1. print msg parameter
        2. return msg parameter
    param : msg : str
    return : str
    """
    print(msg)
    return msg

help(echo)
print(echo.__doc__)

# 2. Scope 범위
# - 함수 안에서 선언되는 변수와 함수 밖에서 선언되는 변수의 범위가 다릅니다.
# - global(전역), local(지역)

### 3. Inner Function
# - 함수가 지역영역에 선언, 함수 안에 함수가 선언

def outer(a, b):
    
    def inner(c, d):
        return c + d
    
    return inner(a, b)

outer(1, 2)

def outer2(a, b):
    
    def inner(c, d):
        return c + d
    
    return inner

outer2(1, 2)(3, 4) # inner(3, 4)

# callback function : 함수를 아규먼트 파라미터로 설정해서 사용

def calc10(func, a, b):
    # code
    a **= 2
    b **= 2
    return func(a, b)

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b
print(calc10(plus, 1, 2)) # 덧셈
print(calc10(minus, 1, 2)) # 뺄셈

# 4. 람다함수
# - 파라미터를 간단한 계산으로 리턴되는 함수 : 삼항연산
def plus2(a, b):
    return a + b

print(plus(1, 2))

plus2 = lambda a, b: a + b
print(plus2(2, 3))

# calc(func, a, b)
#print(calc(lambda a, b: a * b, 3, 4))
#print(calc(5, 6))

# 5. map, filter, reduce
# - map : 순서가 있는 데이터 집합에서 모든 값에 함수를 적용시킨 결과를 출력

ls = [1, 2, 3, 4]

def odd_even(num):
    return "odd" if num % 2 else "even"

print(odd_even(3), odd_even(4))

print(list(map(odd_even, ls)))

# input 함수로 구분자는 " "으로 여러개의 숫자를 입력 받습니다.
# str.split(" ") 리스트로 만들고
# 만들어진 리스트의 값들을 int 형변환

datas = input("insert numbers : ")
result = datas.split(" ")
print(result)

result = list(map(int, result))
print(result)

# Rilter
# - 리스트 데이터에서 특정 조건에 맞는 value만 남기는 함수
ls = range(10)
# 홀수만 출력
print(list(filter(lambda data: True if data % 2 else False, ls)))

# Reduce
# - 리스트 데이터를 처음부터 순서대로 특정 함수를 실행하여 결과를 누적시켜 주는 함수

from functools import reduce
ls = [3, 1, 2, 4, 5]
print(reduce(lambda x, y: x + y, ls))

### 6. Decorlator
#- 함수에서 코드를 바꾸지 않고 기능을 추가하거나 수정하고 싶을때 사용하는 문법

"""
def a():
    code_1
    code_2
    code_3
    
def b():
    code_1
    code_4
    code_3
"""
# - 데코레이터의 사용

"""
def c(func):
    def wrapper(*args, **kwargs):
        code_1
        result = func(*args, **kwargs)
        code_3
        return result
    return wrapper

@c
def a():
    code_2

@c
def b():
    code_4
"""

# a
def plus4(a, b):
    print("start")                      # code 1
    result = a + b                      # code 2
    print("result : {}".format(result)) # code 3
    return result 

# b
def minus4(a, b):
    print("start")                      # code 1
    result = a - b                      # code 4
    print("result : {}".format(result)) # code 3
    return result  

# c
def disp(func):
    def wrapper(*args, **kwargs):
        print("start")                      # code 1
        result = func(*args, **kwargs)      # code 2, code 4
        print("result : {}".format(result)) # code 3
        return result
    return wrapper

@disp
def plus3(a, b):
    result = a + b                      # code 2
    return result 

plus3(1, 2)


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()        # code 1
        result = func(*args, **kwargs)  # code 2, code 4
        end_time = time.time()          # code 3
        print("running time : {}".format(end_time - start_time)) # code 3
        return result
    return wrapper


# 패스워드를 입력 받아야 함수가 실행되도록하는 데코레이터 작성
def check_password(func):
    def wrapper(*args, **kwargs):
        pw = "dss11"
        # check password
        input_pw = input("insert pw : ")
        if input_pw == pw:
            result = func(*args, **kwargs)
        else:
            result = "not allow!"
        return result 
    return wrapper

@timer
@check_password
def plus5(a, b):
    return a + b

plus5(1, 2)

@check_password
def lotto_func():
    lotto = []
    while True:
        number = random.randint(1, 45)
        if number not in lotto:
            lotto.append(number)
        if len(lotto) >= 6:
            lotto.sort()
            break
    return lotto

lotto_func()