from collections import defaultdict
from collections import deque

numberOfComputers = int(input())
numberOfLinkedComputers = int(input())
linked = []

# generate matrix
graphMatrix = [[0] * numberOfComputers for _ in range(numberOfComputers)]
graphList = defaultdict(list)
allNodes = []
for i in range (0, numberOfLinkedComputers):
  node1, node2 = input().split()
  if int(node1) not in allNodes:
    allNodes.append(int(node1))
  if int(node2) not in allNodes:
    allNodes.append(int(node2))
  graphMatrix[int(node1) - 1][int(node2) - 1] = 1
  graphMatrix[int(node2) - 1][int(node1) - 1] = 1
  graphList[node1].append(node2)

def graphTraverse(g, start):
  visited = deque([])
  mustVisit = deque([start])
  while len(visited) != len(allNodes):
    current = mustVisit.popleft()
    for i in range(0, len(g[current - 1])):
      if g[current - 1][i] == 1:
        if current - 1 != i:
          mustVisit.append(i + 1)
  


print(graphList)
print(allNodes)