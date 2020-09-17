"""
여벌의 체육복은 반드시 1명에게만 빌려줄 수 있다. 
그렇다면.. 전체를 하나의 배열로 만들면 어떨까.
이건 좀 돌아가는 방법이지만.. 그래도 먼저 이 방법을 써보도록한다.
lost 와 reserve에서 각각의 숫자는 index를 나타내므로
그것으로 total을 채운다.
ex) [2,0,2,0,2]
[1,0,2,0,1]
[2,1,0]
"""
def solution(n, lost, reserve):
    answer = 0
    total = []
    for i in (0,n):
        total.append(1)
    for all in reserve:
        total[all] += 1
    for all in lost:
        total[all] -= 1
    #now the total list is finished.
    for i in range(0,len(total)):
        if total[i] == 0:
            if total[i-1]==2 or total[i+1]==2:
                

    return answer