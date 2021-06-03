def BFS(graph, start_node):
  visited = list()
  need_visit = list()

  need_visit.append(start_node)
  count = 0
  while need_visit:
    count += 1
    node = need_visit.pop(0)
    if node not in visited:
      visited.append(node)
      need_visit.extend(graph[node])
  print(count)
  return visited

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']
print(BFS(graph, 'A'))