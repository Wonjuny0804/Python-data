from node import Node

class LinkedListFIFO(object):
    def  __init__(self):
        self.head = None # head
        self.length = 0
        self.tail = None # tail

    # print starting from the head
    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()
     