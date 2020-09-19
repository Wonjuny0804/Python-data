"""
정수 2개를 입력받아 그대로 출력하기
정수(int) 2개를 입력받아 그대로 출력해보자.
input : 1 2
output : 1 2
"""
a,b = input().split()
print(a,b)

# in Python there are some ways you can get multiple inputs
# like in C++ normally you would use, 
# scanf("%d%d", &a,&b);
# in python you would use something like...
# var1, var2 = input().split()