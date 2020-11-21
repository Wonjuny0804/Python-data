# 파이선 예외처리의 이해

# 예외의 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError..
# 문법적으로 에러가 없지만 코드 실행 프로세스에서 발생하는 예외 처리 중요

# SyntaxError : 잘못된 문법

# NameError : 참조 변수 없음

# IndexError : 인덱스 범위 오버

# ZeroDivisionError : 0 나누기 에러

# KeyError

# Value Error : 참조 값이 없을 때 예외

# FileNotFoundError

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외처리 권장(EAFP 코딩 스타일)

#try else except, finally

# 예외 처리 기본
# try               에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1:    여러 개 가능(에러 처리)
# except 에러명2: 
# else:             try 블록의 에러가 없을 경우 실행
# finally:          항상 실행


name = ['Wonjun', 'Wonseok', 'Theo', 'Kiyeon']

try:
    x = 'Wonjun'
    y = name.index(x)
    print("{} Found it! {}".format(x, y+1))
except:
    print("Not found it! = Occurred ValueError!")
else:
    print("oK! else!")



# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Kim':
        print('Ok! pass')
    else:
        raise ValueError
except ValueError:
    print('Raise! Occurred ValueError')
except Exception:
    print('Occurred Exception')
else:
    print('ok! else!')
