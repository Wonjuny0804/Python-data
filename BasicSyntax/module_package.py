"""
summary
- 상속 : 다른 클래스를 받아서 기능을 추가해서 새로운 클래스를 만드는 방법
- super : 부모클래스에서 특정 함수의 코드를 가져오는 방법
- getter, setter : 클래스로 만들어진 객체에 변수값을 수정하거나 출력할때 특정 함수를 통해서 수정하고 
출력하는 방법
- non public(private) : mangling(__) `_(class_name)` 이 붙은 변수로 객체를 생성할때 변경이 되어서
생성
- is a / has a : 클래스를 설계하는 방법
- magic(special) method
    - 비교 : `__eq__`(==),`__ne__`(!=),`__lt__`(<),
            `__gt__`(>),`__le__`(<=),`__ge__`(>=)
    - 연산 : 
        - `__add__`(+),`__sub__`(-),`__mul__`(*),`__truediv__`(/)
        - `__floordiv__`(//), `__mod__`(%), `__pow__`(**)
    - 그외 : `__repr__`, `__str__`

"""
#Integer 객체
class Integer:

    def __init__(self, number):
        self.number = number

    def __add__(self, obj):
        return self.number + obj.number

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self.number)

# account 객체 만들어보기
class Account:

    def __init__(self, asset=0, interest=1.05):
        self.asset = asset
        self.interest = interest

    def draw(self, money):
        if self.asset >= money:
            self.asset -= money
            print("{}원이 인출되었습니다.".format(money))
        else:
            print("인출금이 {}원이 부족합니다.".format(money-self.asset))

    def insert(self, money):
        self.asset += money
        print("{}원이 입금되었습니다.".format(money))

    def add_interest(self):
        self.asset *= self.interest
        print("이자가 지급되었습니다.")

    def __repr__(self):
        return "Account(asset:{}, interest:{}".format(self.asset, self.interest)

account1 = Account(10000)
print(account1)
account1.draw(12000)
account1.draw(3000)
print(account1)
account1.insert(5000)
print(account1)

"""
Module Package
- module : 변수, 함수, 클래스를 모아놓은 (.py) 확장자를 가진 파일
- package : 모듈의 기능을 디렉토리별로 정리해 놓은 개념
"""

# 1. Module
#  - 모듈 생성
#  - 모듈 호출

# 모둘을 생성한다. 
# %%writefile dss.py

num = 1234
def disp1(msg):
    print("disp1", msg)
def disp2(msg):
    print("disp2", msg)

class Calc:
    def plus(self, *args):
        return sum(args)