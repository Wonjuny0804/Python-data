from linkedlistFIFO import LinkedListFIFO
from node import Node

def partList(ll, n):
    more = LinkedListFIFO()
    less = LinkedListFIFO()

    node = ll.head

    while node:
        item = node.value

        if item < n:
            less.addNode(item)
        
        elif item > n:
            more.addNode(item)

        node = node.pointer

    less.addNode(n)
    nodemore = more.head

    while nodemore:
        less.addNode(nodemore.value)

        nodemore = nodemore.pointer

    return less

if __name__ == "__main__":
    ll = LinkedListFIFO()
    l = [6,7,3,4,9,5,1,2,8]
    for i in l:
        ll.addNode(i)

    print("Before:")
    ll._printList()

    print("After:")
    newll = partList(11, 6)
    newll._printList()
    
