"""
AVERAGE
70
60
55
75
95
90
80
80
85
100
총 10줄로 이루어진 sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균
값을 구한 후 평균 값을 result.txt. 파일에 쓰는 프로그램을 작성하시오.
"""
with open("sample.txt","r") as f:
    content = f.readlines()
    total = 0
    count = 0
    for c in content:
        total += int(c)
        count += 1
    
    average = total / count

with open("result.txt", "w") as f:
    f.write(str(average))