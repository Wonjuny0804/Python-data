# Linked List 구현하기

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self, data):
    self.head = Node(data)
  
  def add(self, data):
    if self.head == '':
      self.head = Node(data)
    else:
      node = self.head
      while node.next:
        node = node.next
      node.next = Node(data)
  
  def desc(self):
    node = self.head
    while node:
      print(node.data)
      node = node.next

linkedlist1 = LinkedList(0)
linkedlist1.desc()

# list comprehension
numbers = []
for n in range(0, 10):
  numbers.append(n)

# print([n for n in range(10)])

# 리스트 컴프리헨션 조건걸기
# 짝수만 넣는다. 
# print([n for n in  range(0, 10) if n % 2 == 0])

for i in range(1, 10):
  linkedlist1.add(i)
linkedlist1.desc()