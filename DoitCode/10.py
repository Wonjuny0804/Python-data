"""
Build a Calculator class
"""

class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def sum(self):
        self.total = 0
        for all in self.numbers:
            self.total += all
        return self.total
    
    def avg(self):
        self.AVG = 0
        self.AVG = self.sum()/len(self.numbers)
        return self.AVG
    
cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())