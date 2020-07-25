"""
stack only with nodes
"""

class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

class Stack(object):
    def __init__(self):
        self.head = None
        self.pointer = pointer

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def pop(self):
        if self.count >0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        else:
            print("Stack is empty.")

    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print("Stack is empty")

    def size(self):
        return self.count
    
    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer

        print()

if __name__ == "__main__":
    stack = Stack()
    print("Is the stack empty? {0}".format(stack.isEmpty()))
    print("Adding numbers 0~9 to the stack.")
    for i in range(10):
        stack.push(i)

    stack._printList()
    print("Stack size : {0}".format(stack.size()))
    print("peek : {0}".format(stack.peek()))
    print("pop : {0}".format(stack.pop()))
    print("peek : {0}".format(stack.peek()))
    print("Is the stack empty : {0}".format(stack.isEmpty()))
    stack._printList()