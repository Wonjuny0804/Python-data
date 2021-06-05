# def solution(tickets):
#   return


# def getDeparts(tickets):
#   return [i[0] for i in tickets]

# [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# # 출발과 끝이 다를수도 있다. 
# # 출발이 하나

# # 완전 탐색 알고리즘??
# # 왜 이게 BFS/DFS문제이지??

# def solution(tickets):
#   tickets.sort(reverse=True)
#   routes = dict()
#   for t1, t2 in tickets:
#     if t1 in routes:
#       routes[t1].append(t2)
#     else:
#       routes[t1] = [t2]
#   print(routes)
#   st = ['ICN']
#   answer = []
#   while st:
#     top  = st[-1]
#     if top not in routes or len(routes[top]) == 0:
#       answer.append(st.pop())
#     else:
#       st.append(routes[top].pop())
#   answer.reverse()
#   return answer

# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])

AL = [[] for _ in range(10 + 1)] 
edges = [(1, 2), (1, 4), (1, 5), (2, 3), (3, 4), (3, 7), (4, 6), (5, 6)] 
for s, e in edges: 
  AL[s].append(e) 
  AL[e].append(s)

for i in AL:
  print(i, end='\n')