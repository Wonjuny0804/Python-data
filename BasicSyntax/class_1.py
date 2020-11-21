"""
class : 클래스
    - 변수와 함수를 묶어 놓은 개념
    - 사용 방법
        - 변수와 함수가 들어있는 클래스를 선언
        - 클래스를 객체로 만들어서 클래스 안에 선언된 변수와 함수를 사용

"""
# 1. 기본 클래스의 사용

# Class의 선언
class Calculator:
    
    num1 = 1
    num2 = 2
    
    def plus(self):
        return self.num1 + self.num2
    
    def minus(self):
        return self.num1 - self.num2

# 클래스의 사용
calc = Calculator()
print(calc)

print(calc.num1, calc.num2, calc.plus(), calc.minus())

# self의 의미: 객체 자신
calc2 = Calculator()
calc2.num1 = 10
calc2.plus()

"""
2. 객체지향
    - 실제 세계를 코드에 반영해서 개발하는 방법
    - 여러명의 개발자가 코드를 효율적으로 작성해서 프로젝트를 완성시키기 위한 방법
    - 설계도 작성(class) -> 실제 물건(object)
    - 사용자 정의 데이터 타입

"""

obj = "python"
print(obj.upper())

ls = [1, 3, 2]
print(ls.sort())
print(ls)

print([data for data in dir(calc) if data[:2] != "__"])

"""
3. 생성자
    - 클래스가 객체로 생성될때 실행되는 함수
    - 변수(재료)를 추가할때 사용됩니다.
"""

class Calculator2:

    # 생성자 함수: __init__
    def __init__(self, num1, num2=10):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        pass

    def minus(self):
        pass

