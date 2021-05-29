class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BST:
  def __init__(self, value):
    self.root = Node(value)
  
  def insert(self, value):
    self.current_node = self.head
    while True:
      if value < self.current_node.value:
        if self.current_node.left:
          self.current_node = self.current_node.left
        else:
          self.current_node.left = Node(value)
          break
      else:
        if self.current_node.right:
          self.current_node = self.current_node.right
        else:
          self.current_node.right = Node(value)
          break
  
  # Binary Search
  def search(self, value):
    self.current_node = self.root

    while self.current_node:
      if self.current_node.value == value:
        return True
      elif value < self.current_node.value:
        self.current_node = self.current_node.left
      else:
        self.current_node = self.current_node.right
    return False

  # delete a Node
  def delete(self, value):
    # Tree에서 노드를 삭제할때는 경우의 수를 생각해야한다. 
    """
    1. 삭제할 노드가 리프노드인 경우
    2. 삭제할 노드가 자식 노드가 하나인 경우
    3. 삭제할 노드가 자식 노드가 둘인 경우
    """
    Found = False
    self.current_node = self.root
    self.parent_node = self.root
    while self.current_node:
      if self.current_node.value == value:
        Found = True
        break
      elif value < self.current_node.value:
        self.parent_node = self.current_node
        self.current_node = self.current_node.left
      else:
        self.parent_node = self.current_node
        self.current_node = self.current_node.right
    
    if Found == False:
      return False
    
    # while을 빠져나오면 parent와 current는 우리가 원하는 위치에 있다.
    if self.current_node.left == None and self.current_node.right == None:
      if value < self.parent_node.value:
        self.parent_node.left = None
      else:
        self.parent_node.right = None
    
    elif self.current_node.left != None and self.current_node.right == None:
      if value < self.parent_node.value:
        self.parent_node.left = self.current_node.left
      else:
        self.parent_node.right = self.current_node.left
    elif self.current_node.left == None and self.current_node.right != None:
      if value < self.parent_node.value:
        self.parent_node.left = self.current_node.right
      else:
        self.parent_node.right = self.current_node.right

    elif self.current_node.left != None and self.current_node.right != None:
      if value < self.parent_node.value:
        self.change_node = self.current_node.right
        self.chagne_node_parent = self.current_node.right
        while self.change_node.left:
          self.change_node_parent = self.change_node
          self.change_node = self.change_node.left
        if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
        else:
            self.change_node_parent.left = None
        self.parent_node.left = self.change_node
        self.change_node.right = self.current_node.right
        self.change_node.left = self.change_node.left
    # 가장 복잡한 경우의 수이다. 노드가 자식이 두 개일때
    """
    노드가 자식이 두 개 일때는 오른쪽 노드 중 가장 작은 노드로 그 자리를 대신해야 한다.
    또는 왼쪽 노드들 중에서 가장 큰 노드로 그 자리를 대신하도록 해야한다.  
    """

SampleBST = BST(1)
SampleBST.insert(2)
SampleBST.insert(0)
SampleBST.insert(-1)
SampleBST.insert(4)
print(SampleBST.search(6))