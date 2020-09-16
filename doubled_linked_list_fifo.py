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
    
    def _delete(self, node):
        self.length -= 1
        node.previous.pointer = node.pointer
        if not node.pointer:
            self.tail = node.previous

    def _find(self, index):
        node = self.head
        i = 0
        while node and i < index:
            node = node.pointer
            i += 1
        return node, i

    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self._deleteFirst()()
        else:
            node, i = self._find(index)
            if i == index:
                self._delete(node)
            else:
                print("Index {} node does not exsist.".format(index))
    