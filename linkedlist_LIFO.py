from node import Node

class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0

    # print each node from the head
    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()

    # 이전 노드(prev)를 기반으로 노드(node)를 삭제한다. 
    def _delete(self, prev, node):
        self.length -= 1
        if not prev:
            self.head = node.pointer
        else:
            prev.pointer = node.pointer

        