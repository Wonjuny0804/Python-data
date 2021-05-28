# 먼저 Node하나의 클래스르 정의한다.

class Node:
  # 생성자 함수
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
  
node1 = Node(1)
node2 = Node(2)
node1.next = node2 # 서로 연결
# 가장 앞에 있는 node는 head로 저장
head = node1

class NodeManagement:
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
  
  def delete(self, data):
    if self.head == '':
      print("해당 값을 가진 노드가 없습니다.")
      return
    
    if self.head.data == data:
      temp = self.head
      self.head = self.head.next
      del temp # 객체 삭제
    else: 
      node = self.head
      while node.next:
        if node.next.data == data:
          temp = node.next
          node.next = node.next.next
          del temp
        else:
          node = node.next


linkedlist1 = NodeManagement(0)
linkedlist1.desc()

# data 넣기
for data in range(1, 10):
  linkedlist1.add(data)
linkedlist1.desc()