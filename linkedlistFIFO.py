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

    # add new node, if there is tail the tail directs to the new node
    def _add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node
        self.tail = node
    
    # add new node
    def addNode(self, value):
        if not self.head:
            self._addFirst(value)
        else:
            self._add(value)

    # find node by index
    def _find(self, index):
        prev = None
        node = self.head
        i = 0

        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    # find node by value
    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    # delete according to index
    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev :
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print("index {0} does not exist.".format(index))