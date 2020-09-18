"""
피보나치 함수
첫 번쨰 항의 값이 0이고 두 번째 항의 값이 1일때, 
이후에 이어지는 항은 이전의 두 항을 더한 겁으로 이루어지는
수열을 피보나치 수열이라고 한다. 
입력을 정수 n으로 받았을 때, n이하까지의 피보나치 수열을 출력하는
함수를 작성해 보자.
"""
def fib(n):
    lst = [0,1]

    while len(lst)<n:
        lst.append(lst[-1]+lst[-2])
        # the last two elements of the list are the last
        # two things that needs to be added.
        # As like a fibonacci.
    print(lst)
