"""
1018: 시간 입력받아 그대로 출력하기

어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하느 연습을
해보자.

입력: 시(hour)와 분(minute)이 ":"으로 구분되어 있다. 
출력 : 입력받은 시간을 "시:분" 형식으로 출력한다.

"""
# it is time to use input().split()
# inside split() you can put in anything that would
# seperate the data

hour, minute = input().split(":")
print(hour+":"+minute)