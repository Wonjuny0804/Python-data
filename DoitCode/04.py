'''
리스트 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
다음 리스트에서 50점 이상의 점수의 총합을 구하라.
'''
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
total = 0
for score in A:
    if score >= 50:
        total += score
print(total)