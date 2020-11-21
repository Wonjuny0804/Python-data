"""
### 파이썬의 기본 문법
- 변수 선언, 식별자, 자료형, 형변환, 연산자 학습
"""

# 1. 주석(comment)과 출력(print)

# 주석 : 앞에 0을 붙이면 코드로 실행이 안됩니다.
# 코드에 대한 설명이나 중간에 코드를 실행시키고 싶지 않을때 사용
"""
 2. 변수 선언
- RAM 저장공간에 값을 할당하는 행위
"""
d, e = 3, 4
f = g = 5

"""
3. 식별자
- 변수, 함수, 클래스, 모듈 등의 이름을 식별자라고 합니다. 
    - 소문자, 대문자, 숫자, 언더스코어(_)를 사용
    - 가장 앞에 숫자 사용 불가
    - 예약어의 사용 불가 : def, class, try, except...
    - 컨벤션
        - snake case : fast_campus : 변수, 함수 선언에 사용
        - camel case : FastCampus, fastCampus : 클래스를 선언할 때 사용
"""

# def = 1 this is not possible(invalid syntax)

"""
4. 데이터 타입
- RAM 저장공간을 효율적으로 사용하기 위해서 저장공간의 타입을 설정
- 동적타이핑
    - 변수 선언시 저장되는 값에 따라서 자동으로 데이터 타입이 설정
- 기본 데이터 타입 : int, float, bool, str
- 컬렉션 데이터 타입 : list, tuple, dict
"""
a = 1
# int a = 1
b = "python"
print(type(a), type(b))

# 기본 데이터 타입 : int, float, bool, str
a = 1
b = 1.2
c = True # False
d = "data"
print(type(a), type(b), type(c), type(d))

# 오프셋 인덱스 : 마스크, 마스킹 : []
# 문자열은 순서가 있는 문자들의 집합

g = "abcdefg"

print(g[2], g[-2], g[2:5], g[:2], g[3:], g[-2:], g[::3], g[::-1])

numbers = '123456789'
result = numbers[::2]
print(result[::1])


"""
컬렉션 데이터 타입 : list, tuple, dict
- list [] : 순서가 있는 수정이 가능한 데이터 타입
- tuple () : 순서가 있는 수정이 불가능한 데이터 타입
- dict {} : 순서가 없고 키:값 으로 구성되어 있는 데이터 타입
"""

# list
ls = [1, 2, 3, "four", [5, 6], True, 1.2]
print(type(ls), ls)


# offset index 사용이 가능
print(ls[3], ls[1:3], ls[::-1])

# list 함수
ls = [1, 5, 2, 4]
#append: 가장 뒤에 값을 추가
ls.append(3)
print(ls)

#sort: 오름차순으로 정렬
ls.sort()
print(ls)
print(ls[::-1])

# pop : 가장 마지막 데이터를 출력하고 출력한 데이터를 삭제
# ctrl + enter : 현재 셀을 계속 실행
num = ls.pop()
print(num, ls)

# 리스트의 복사
ls1 = [1, 2, 3]
ls2 = ls1 # 얕은 복사 : 주소값 복사
print(ls1, ls2)

ls1[2] = 5
ls3 = ls1.copy()
print(ls1, ls3)

ls1[2] = 10
print(ls1, ls3)

"""
Tuple ()
- 리스트와 같지만 수정이 불가능한 데이터 타입
- 튜플은 리스트보다 같은 데이터를 가졌을때 공간을 적게 사용
"""

tp1 = 1, 2, 3
tp2 = (4, 5, 6)
print(type(tp1), type(tp2), tp1, tp2)

a, b = 1, 2
print(a, b)

# offset index 사용
print(tp1[1], tp1[::-1])

# 리스트와 튜플의 저장공간 차이 비교
import sys

ls = [1, 2, 3]
tp = (1, 2, 3)

print(sys.getsizeof(ls), sys.getsizeof(tp))

"""
dict {}
- 순서가 없고 {key:value}으로 구성되어 있는 데이터 타입
"""
# 선언 : 키는 정수, 문자열 데이터 타입만 사용이 가능
# 인덱스 대신 키를 사용
dic = {
    1: "one",
    "two" : 2,
    "three": [1, 2, 3], 
}
print(type(dic), dic)

print(dic[1], dic["three"])

dic["two"] = 123
print(dic)

# 아래의 데이터를 list와 dict로 선언
# 도시 : seoul, busan, daegu
# 인구 : 9,700,000, 3,400,000, 2,400,000

# 리스트
city = ["seoul", "busan", "daegu"]
population = [9700000, 3400000, 2400000]

# 딕셔너리
data = {
    "seoul": 9700000,
    "busan": 3400000,
    "daegu": 2400000,
}

print(sum(population))
print(sum(data.values()))

"""
5. 형변환
- 데이터 타입을 변환하는 방법
- int, float, bool, str, list, tuple, dict
"""

a = 1
b = "2"
print(a + int(b))
print(str(a)+b)

list(data.values())

print(city, population)

# zip : 같은 인덱스 데이터끼리 묶어주는 함수
print(list(zip(city, population)))

result = dict(list(zip(city, population)))
print(result)

data1 = list(result.keys())
data2 = list(result.values())
print(data1, data2)

"""
6. 연산자
- 산술연산자 : +, -, *, /, //, %, **
- 할당연산자 : 변수에 누적시켜서 연산 : +=, //=, **= ...
- 비교연산자 : >, <, ==, !=, <=, >= : 결과로 True, False
- 논리연산자 : True, False 를 연산 : or, and, not
- 멤버연산자 : 특정 데이터가 있는지 확인할때 사용 : not in, in
"""
a = 1
b = 2
c = a + b
print(c)

# 산술 연산
print((1 + 4) / 2 ** 2)

# 할당 연산
a = 10
# a = a + 10
# a = a + 10
a += 10
a += 10
print(a)

# 비교 연산
print(a, b)
print(a < b, a == b, a != b)

# 논리 연산
print(True and False, True or False, not (True or False))

# 멤버 연산
ls = ["jin", "andy", "jhon"]

print("andy" in ls, "anchel" in ls, "jhon" not in ls)

