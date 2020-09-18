"""
Q2 딕셔너리 값 추출하기
a = {'A':90, 'B':80}
a 딕셔너리에는 'C'라는 key가 없으므로 위와 같은 오류가 발생한다. 
'C'에 해당하는 key값이 없을 경우 오류 대신 70을 얻을 수 있도록 수정하시오.
"""

a = {'A':90,'B':80}
a['C'] = 70 
# So this is how you put key and value in to a dictionary
print(a['C'])