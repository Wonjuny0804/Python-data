from datetime import date
def solution (a, b) :
  answer = ''
  d = date(2021, a, b).isoweekday()
  if d == 1:
    return 'MON'
  elif d == 2:
    return 'TUE'
  elif d == 3:
    return 'WED'
  elif d == 4:
    return 'THU'
  elif d == 5:
    return 'FRI'
  elif d == 6:
    return 'SAT'
  else:
    return 'SUN'
print(solution(5, 24))