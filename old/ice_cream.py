def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False
N, M = list(map(int, input().split())) # N 세로 길이, M 가로 길이

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)





