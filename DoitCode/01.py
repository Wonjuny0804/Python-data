"""
Q1 문자열 바꾸기
문자열
a:b:c:d
split과 join을 이용해서 
a#b#c#d로 고친다.
"""
first = "a:b:c:d"
second=first.split(":")
third="#".join(second)
#-> You should try to remember how to use 'split' and 'join'
print(third)