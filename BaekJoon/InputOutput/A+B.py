# input은 input함수를 쓴다. input함수는 enter를 받기 전까지 입력을 받는다. 따라서 split으로 입력받은 것을 나눈다. 
a, b = input().split(' ')
print(int(a) + int(b))
