# Doubly LinkedList

class Node:
  def __init__(self, data, prev=None, next=None):
    self.data = data
    self.prev = prev
    self.next = next

class DoublyLinkedList:
  def __init__(self, data):
    self.head = Node(data)
    self.tail = self.head

  def insert(self, data):
    if self.head == '':
      return
    
    node = self.head
    new = Node(data)
    while node.next:
      node = node.next
    node.next = new
    new.prev = node
    self.tail = new

  def desc(self):
    if self.head == '':
      return
    
    node = self.head
    while node:
      print(node.data, end=" ")
      node = node.next
  
  def delete(self, data):
    node = self.head
    while node.data != data:
      node = node.next
      if node == self.tail:
        if node.data != data:
          return False
    # 세가지 경우의 수 
    if node.prev and node.next:
      node.prev.next = node.next
      node.next.prev = node.prev
    elif not node.prev and node.next:
      node.next.prev = node.prev
      self.head = node.next
    elif node.prev and not node.next:
      node.prev.next = node.next
      self.tail = node.prev
  
  def insertFrontOf(self, data, new):
    if self.head == '':
      return 
    
    node = self.head
    while node.data != data:
      node = node.next
    
    frontNew = Node(new)
    # 두 가지 경우의 수
    if not node.prev:
      node.prev = frontNew
      frontNew.next = node
      self.head = frontNew
    else:
      node.prev.next = frontNew
      frontNew.prev = node.prev
      node.prev = frontNew
      frontNew.next = node
    
  def edit(self, data, new):
    if self.head == '': return

    node = self.head
    while node.data != data:
      node = node.next
      if node == self.tail:
        if node.data != data:
          return False

    node.data = new

example = DoublyLinkedList(0)
for i in range(1, 11):
  example.insert(i)
example.desc()
print('', end='\n')
example.insert(11)
example.desc()
print('', end='\n')
example.delete(0)
example.delete(2)
example.delete(10)
example.delete(11)
example.desc()
print('', end='\n')
example.insertFrontOf(5, 42)
example.insertFrontOf(1, 42)
print('', end='\n')
example.desc()
example.edit(42, 5)
print('', end='\n')
example.desc()