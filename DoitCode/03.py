"""
다음과 같은 리스트 a가 있다.
a = [1,2,3]
리스트 a에 [4,5]를 +기호를 사용하여 더한 결과는 다음과 같다. 
a=[1,2,3]
a=a+[4,5]
print(a)
[1,2,3,4,5]

리스트 a에 [4,5]를 extend를 사용하여 더한 결과는 다음과 같다. 
"""
a = [1,2,3]
a = a + [4, 5]
print(a)
b = [1, 2, 3]
b.extend([4, 5])
print(b)