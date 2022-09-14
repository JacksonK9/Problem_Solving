from collections import deque

def bfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M or graph[x][y] == 1:
        return 0 
    queue = deque()
    queue.append([x, y])
    while queue:
        [now_x, now_y] = queue.popleft()
        print(now_x, now_y)
        graph[now_x][now_y] = 1
        if graph[now_x + 1][now_y] == 0:
            queue.append([now_x + 1, now_y])
        if graph[now_x - 1][now_y] == 0:
            queue.append([now_x - 1, now_y])
        if graph[now_x][now_y + 1] == 0:
            queue.append([now_x, now_y + 1])
        if graph[now_x][now_y + 1] == 0:
            queue.append([now_x, now_y + 1])
        
    return 1
    

N, M = list(map(int, input().split())) 

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

result = 0
for i in range(N):
    for j in range(M):
        result += bfs(i, j)
print(result)