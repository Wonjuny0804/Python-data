from linkedlistFIFO import LinkedListFIFO

class DNode(object):
    def __init__(self, value=None, pointer=None, previous=None):
        self.value = value
        self.pointer = pointer
        self.previous = previous

class DLinkedList(LinkedListFIFO):
    def printListInverse(self):
        node = self.tail
        while node:
            print(node.value, end=" ")
            try:
                node = node.previous
            except AttributeError:
                break
        print()

    def _add(self, value):
        self.length += 1
        node = DNode(value)
        if self.tail:
            self.tail.pointer = node
            node.previous = self.tail
        self.tail = node
    
    