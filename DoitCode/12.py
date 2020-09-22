"""
Q12
error and exceptions
"""

result = 0
try:
    [1,2,3][3]
    "a"+1
    4/0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)
    
"""
the result is 7
because [1,2,3][3] is an IndexError
3 + 4 = 7
"""