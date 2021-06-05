def graph(width, height):
  smalls = [0] * width
  outers = []
  for i in range(0, height):
    outers.append(smalls);
  return outers

[[0] * row for i in range(column)]
def solution(testCase, row, column, cabbages):
  # create Graph

  M, N, K = map(int, input().split())
  matrix = [[0] * M for _ in range(N)]
  cnt = 0
  farm = graph(row, column)
  print(farm)
  print(len(cabbages))
  for i in range(0, len(cabbages)):
    print(farm[cabbages[i][0]][cabbages[i][1]])
    farm[cabbages[i][0]][cabbages[i][1]] = 1
  
  print(farm)
haha = [
  [0, 0],
  [1, 0],
  [1, 1],
  [4, 2],
  [4, 3],
  [4, 5],
  [2, 4],
  [3, 4],
  [7, 4],
  [8, 4],
  [9, 4],
  [7, 5],
  [8, 5],
  [9, 5],
  [7, 6],
  [8, 6],
  [9, 6],
]
solution(2, 10, 8, haha)


"""
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
"""

# make a graph

