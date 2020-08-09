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
    
    # add node in the first place
    def _addFirst(self, value):
        self.length = 1
        node = Node(value)
        self.head = node
        self.tail = node
    
    # delete first place node
    def _deleteFirst(self):
        self.length = 0
        self.head = None
        self.tail = None
        print(" Linked-List is empty.")

    
