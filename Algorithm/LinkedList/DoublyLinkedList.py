class Node:
  def __init__(self, data, prev=None, next=None):
    self.prev = prev
    self.data = data
    self.next = next

class DoublyLinkedList:
  def __init__(self, data):
    self.head = Node(data)
    self.tail = self.head
  
  def insert(self, data):
    if self.head == None:
      self.head = Node(data)
      self.tail = self.head
    else:
      node = self.head
      while node.next:
        node = node.next
      new = Node(data)
      node.next = new
      new.prev = node
      self.tail = new
  
  def desc(self):
    node = self.head
    while node:
      print(node.data, end=' ')
      node = node.next

  def delete(self, data):
    if self.head == None:
      return
    
    node = self.head
    if node.data == data:
      temp = self.head
      self.head = node.next
      self.head.prev = None
      del temp
    else:
      while node.data != data:
        node = node.next
        if not node:
          return "데이터가 존재하지 않습니다."
      temp = node
      node.prev.next = node.next
      if node.next:
        node.next.prev = node.prev
      del temp
    
  # 특정 노드 앞에 데이터 삽입하기
  def insertBefore(self, before, data):
    if self.head == '':
      return
    
    node = self.head
    if before == node.data:
      inserting = Node(data)

      inserting.next = node
      node.prev = inserting
      self.head = inserting
    else:
      while node.data != before:
        node = node.next
      inserting = Node(data)
      node.prev.next = inserting
      inserting.prev = node.prev

      node.prev = inserting
      inserting.next = node

  def insertToFront(self, data):
    if self.head == '':
      return
    
    node = self.head
    inserting = Node(data)
    inserting.next = node
    node.prev = inserting.next
    self.head = inserting
DLL = DoublyLinkedList(0)

for i in range(1, 5):
  DLL.insert(i)
DLL.desc()

DLL.delete(9)
print('',end='\n')
DLL.desc()

DLL.delete(0)
print('',end='\n')
DLL.desc()

DLL.delete(11)
print('',end='\n')
DLL.desc()

DLL.insert(10)
print('',end='\n')
DLL.desc()

DLL.insertBefore(2, 4)
print('', end='\n')
DLL.desc()

DLL.insertBefore(1, 4)
print('', end='\n')
DLL.desc()

DLL.insertToFront(0)
print('', end='\n')
DLL.desc()