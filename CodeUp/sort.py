"""
1. K번째수
"""
def solution(array, commands):
    answer = []
   

    for all in commands:
        I = array[all[0]-1:all[1]]
        I.sort()
        answer.append(I[all[2]-1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))