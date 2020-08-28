from stack import Stack

class SetOfStacks(Stack):
    def __init__(self, capacity=4):
        self.setofstacks = []
        self.items = []
        self.capacity = capacity

    def push(self, value):
        if self.size() >= self.capacity:
            self.setofstacks.append(self.items)
            self.items = []

        self.items.append(value)
    
    def pop(self):
        value = self.items.pop()
        if self.isEmpty() and self.setofstacks:
            self.items = self.setofstacks.pop()
        return value
    
    def sizeStack(self):
        return len(self.satofstacks) * self.capacity + self.size()

    def __repr__(self):
        aux = []
        for s in self.setofstacks:
            aux.extend(s)
        aux.extend(self.items)
        return repr(aux)