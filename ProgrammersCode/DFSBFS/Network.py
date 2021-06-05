def dfs(x, y, n, computers):
    computers[x][y] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if (0 <= nx < n and 0 <= ny < n):
            x, y= nx, ny
            if computers[nx][ny] == 1:
                dfs(nx, ny, n, computers)

def solution(n, computers):
    answer = 0
    for i in range(n) :
        for j in range(n) :
            if computers[i][j] == 1 :
                dfs(i, j, n, computers)
                answer += 1
    dfs(0, 0, n, computers)
    return answer

# def solution(n, computers):
#     answer = 0
#     visited = [False for _ in range(n)]
#     for i in range(n) :
#         if visited[i] == False :
#             dfs(n, i, computers, visited) 
#             answer +=1 

#     return answer


# def dfs(n, i, computers, visited) :
#     visited[i] = True
#     for j in range(n) :
#         if (i!=j and computers[i][j]==1) :
#             if visited[j] == False :
#                 dfs(n, j, computers, visited)