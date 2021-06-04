# 리스트를 활용한 DFS
# 깊이가 우선적으로 깊은 것부터 방문을 한다.
def dfs(graph, start_node):
  need_visited,visited = list(), list()

  need_visited.append(start_node)

  while need_visited:

    node = need_visited.pop()

    if node not in visited:

      visited.append(node)

      need_visited.extend(graph[node])

  return visited

# deque를 이용한 구현
def dfs2(graph, start_node):
  from collections import deque

  need_visited = deque()
  visited = list()

  need_visited.append(start_node)
  while need_visited:
    
    node = need_visited.popleft()

    if node not in visited:

      visited.append(node)
      need_visited.extend(graph[node])
  
  return visited

# 재귀를 이용한 구현
def dfs_recursive(graph, start, visited = []):
  visited.append(start)

  for node in graph[start]:
    if node not in visited:
      dfs_recursive(graph, node, visited)
  return visited