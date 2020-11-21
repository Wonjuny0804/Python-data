"""
summary
- function
    - docstring
    - scope : 전역, 지역 : global
    - inner function : 함수안에 함수를 선언
    - lambda function : 함수 안에 함수를 선언
    - decorator : 특정 기능을 데코레이터 함수로 만들어 함수에 특정 기능을 적용하는 방법
- class
    - 변수와 함수들이 모여있는 집합
    - 기본 클래스 사용법
        - 클래스 선언 -> 객체로 만듦 -> 객체에 함수를 호출
    - 생성자 함수
        - 클래스가 객체로 만들어질때 객체에 선언되는 변수를 설정하는 방법
"""
user_datas = [
    {"user": "test", "pw":"1234", "count": 0},
    {"user": "python", "pw": "5678", "count": 0},
]

ls = ["a", "b", "c"]
print(list(range(len(ls))))
print(list(zip(range(len(ls)), ls)))
for idx, data in list(zip(range(len(ls)), ls)):
    print(idx, data)

list(enumerate(user_datas))

# user data 를 입력 받아서 아이디와 패스워드를 체크하는 데코레이터 함수를 코드로 작성하세요.
# 로그인 될때마다 count를 1씩 증가
def need_login(func):
    def wrapper(*args, **kwargs):
        # 아이디 패스워드 입력
        user, pw = tuple(input("insert user pw : ").split(" "))
        
        # 존재하는 아이디, 패스워드 확인
        # for idx, user_data in zip(range(len(user_datas)), user_datas):
        for idx, user_data in enumerate(user_datas):
            
            if (user_data["user"] == user) and (user_data["pw"] == pw):
                
                # count 데이터 추가 
                user_datas[idx]["count"] += 1
                
                # 함수 실행
                return func(*args, **kwargs)
            
        return "wrong login data!"
    return wrapper

@need_login
def plus(num1, num2):
    return num1 + num2

plus(1, 2)

print(user_datas)

# Starcraft Marine class
class Marine:
    def __init__(self, max_health=40, attack_pow=5):
        self.health = max_health
        self.max_health = max_health
        self.attack_pow = attack_pow

    def attack(self, unit):
        unit.health =- self.attack_pow
        if unit.health <= 0:
            unit.health = 0
            print("dead")
        return unit.health

marine_1 = Marine()
marine_2 = Marine()
marine_2_h = marine_1.attack(marine_2) # 여러번 공격하면 marine_2의 체력이 계속 감소
print(marine_2_h)
print(marine_1.health, marine_1.attack_pow)

# 메딕 : heal_pow, heal(unit)
class Medic:
    
    def __init__(self, max_health=40, heal_pow=6):
        self.health = max_health
        self.max_health = max_health
        self.heal_pow = heal_pow
        
    def heal(self, unit):
        if unit.health > 0:
            unit.health += self.heal_pow
            if unit.health >= unit.max_health:
                unit.health = unit.max_health
        else:
            print("already dead")

medic = Medic()
marine_1.attack(marine_2)

print(marine_1.health, marine_2.health)
print(medic.heal(marine_2))
marine_3 = Marine(attack_pow=25)
marine_3.attack(marine_1)

print(marine_1.health)

"""
1. 상속
- 클래스의 기능을 가져다가 기능을 수정하거나 추가할때 사용하는 방법
"""

class Calculator:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def plus(self):
        return self.num1 + self.num2

calc = Calculator(1, 2)
calc.plus()

# minus 기능을 추가한 계산기
class Calculator2:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def plus(self):
        return self.num1 + self.num2
    
    def minus(self):
        return self.num1 - self.num2

calc2 = Calculator2(1, 2)
calc2.plus(), calc2.minus()

# 상속을 사용하여 minus 함수 추가
class Calculator3(Calculator):
    def minus(self):
        return self.num1 - self.num2

calc3 = Calculator3(1, 2)
print(calc3.plus(), calc3.minus())

# 메서드 오버라이딩
class Calulator4(Calculator3):
    def plus(self):
        return self.num1**2 + self.num2**2

calc4 = Calulator4(1, 2)
print(calc4.plus())

class Iphone1:
    def calling(self):
        print("calling")

class Iphone2(Iphone1):
    def send_msg(self):
        print("send_msg")

class Iphone3(Iphone2):
    def internet(self):
        print("internet")


"""
다중 상속
"""
class Galuxy:
    def show_img(self):
        print("show_img")
class DssPhone(Iphone3, Galuxy):
    def camera(self):
        print("camera")
dss_phone = DssPhone()
print([func for func in dir(dss_phone) if func[:2] != "__"])

"""
super
- 부모 클래스에서 사용된 함수의 코드를 가져다가 자식 클래스의 함수에서 재사용할때
사용한다.
"""
"""
class A:
    def plus(self):
        code1
    
class B(A):
    def minus(self):
        code1 # super().plus()
        code2
"""

class Marine1:
    
    def __init__(self):
        self.health = 40
        self.attack_pow = 5
    
    def attack(self, unit):
        unit.health -= self.attack_pow
        if unit.health <= 0:
            unit.health = 0

class Marine2(Marine1):
    
    def __init__(self):
#         self.health = 40
#         self.attack_pow = 5
        super().__init__()
        self.max_health = 40

marine5 = Marine2()
print(marine5.health, marine5.attack_pow, marine5.max_health)

"""
3. class의 getter, setter
- 객체의 내부 변수에 접근할때 특정 로직을 거쳐서 접근시키는 방법
"""

class User:
    def __init__(self, first_name):
        self.first_name = first_name

    def setter(self, first_name):
        if len(first_name) >= 3:
            self.first_name = first_name
        else:
            print("error")

    def getter(self):
        print("getter")
        return self.first_name.upper()

    name = property(getter, setter)

user1 = User("andy")
print(user1.first_name)

# setter 함수 실행
user1.name = "jhon"

print(user1.first_name)

# getter 함수 실행
print(user1.name)

"""
4. non public
- mangling 이라는 방법으로 다이렉트로 객체의 변수에 접근하지 못하게 하는 방법

"""
class Calculator11:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.__num2 = num2

    def getter(self):
        return self.__num2
    
    # num2에 0이 들어가지 않도록 함
    def setter(self, num2):
        num2 = 1 if num2 == 0 else num2
        self.__num2 = num2
    
    def __disp(self):
        print(self.num1, self.__num2)
    
    def div(self):
        self.__disp()
        return self.num1 / self.__num2
    
    number2 = property(getter, setter)

calc3 = Calculator11(1, 2)
calc3.div()


calc3.number2 = 0
print(calc3.number2)

print(calc3.__num2)


"""
5. is a & has a
- 클래스를 설계하는 개념
- A is a B
    - A는 B이다. 상속을 이용해서 클래스를 만드는 방법
- A has a B
    - A는 B를 가진다. A가 B객체를 가지고 클래스를 만드는 방법
"""
# 사람 : 이름, 이메일, 정보출력()

# is a
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Person2(Person):
    def info(self):
        print(self.name, self.email)

p = Person2("andy", "andy@gmail.com")
p.info()

# has a
class Name:
    def __init__(self, name):
        self.name_str = name
class Email:
    def __init__(self, email):
        self.email_str = email

class Person3:
    def __init__(self, name_obj, email_obj):
        self.name = name_obj
        self.email = email_obj
    def info(self):
        print(name.name_str, email.email_str)

name = Name("andy")
email = Email("andy@gmail.com")
pt = Person3(name, email)

pt.info()


"test".__eq__("test")
print(1+2)
print("1"+"2")

class Txt:
    def __init__(self, txt):
        self.txt = txt
        
    def __eq__(self, txt_obj):
        return self.txt.lower() == txt_obj.txt.lower()
    
    def __repr__(self):
        return "Txt(txt={})".format(self.txt)
    
    def __str__(self):
        return self.txt

t1 = Txt("python")
t2 = Txt("Python")
t3 = t1

print(t1 == t2, t1 == t3, t2 == t3)
print(t1)
print(range(5))

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show" Method!'

class BmwCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name
    
class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show(self):
        super().show()
        return 'Car Info: %s %s %s' % (self.car_name, self.color, self.type)

    def show_model(self):
        return 'Your Car Name : %s' % self.car_name


model1 = BmwCar('720i', 'sedan', 'navy')

print(model1.color)
print(model1.type)
print(model1.car_name)
print(model1.show_model())
print(model1.show())

model2 = BmwCar('z4', 'coupe', 'red')
print(model2.show())

#Inheritance Info
print('Inheritance Info : ', BmwCar.mro())
print('Inheritance Info : ', BenzCar.mro())


