"""
1019 연월일 입력받아 그대로 출력하기
년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.

입력: 연, 월, 일이 . 으로 구분되어 있다. 
입력받은 연, 월, 일을 yyyy.mm.dd 형식으로 출력한다. 

출력: 월, 일은 2칸씩 사용해서 한 자리 수인 경우 앞에 0을 붙여서
출력한다. 
"""
year, month, date = input().split(".")
print(year+"."+month.rjust(2,'0')+"."+date.rjust(2,'0'))
print(year+"."+"%02d"% int(month)+"."+"%02d"% int(date))