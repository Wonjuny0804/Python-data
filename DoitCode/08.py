"""
역순저장
다음과 같음 파일 abc.txt를 생성한다.
AAA
BBB
CCC
DDD
EEE

이 파일을 다음과 같이 역순으로 저장하시오.

EEE
DDD
CCC
BBB
AAA
"""
NumOfLines = 0

with open("abc.txt", "w") as f:
    f.write("AAA\n")
    f.write("BBB\n")
    f.write("CCC\n")
    f.write("DDD\n")
    f.write("EEE\n")

with open("abc.txt", "r") as b:
    content = b.readlines()
    
    for c in content:
        NumOfLines += 1
print(NumOfLines)
print(content)
content = content[::-1]
print(content)
with open("abc.txt", "w") as f:
    for c in content:
        f.write(c)