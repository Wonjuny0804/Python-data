from linkedlistFIFO import LinkedListFIFO
from node import Node

def partList(ll, n):
    more = LinkedListFIFO()
    less = LinkedListFIFO()

    node = ll.head

    while node:
        item = node.value
        