### 전형적인 BFS로 최소 이동 거리 계산하는 문제

''' 
input
5 6
101010
111111
000001
111111
111111

output
10
'''

from collections import deque
import time

def isavailable(x, y):
    if x < 0 or x >= N or y < 0 or y >= M or graph[x][y] == 0:
        return False
    return True

def bfs(x, y):
    result = 1
    queue = deque([[x, y]])
    while queue:
        xn, yn = queue.popleft()
        if xn == N - 1 and yn == M - 1:
            return result
        graph[xn][yn] = 0
        if isavailable(xn + 1, yn) or isavailable(xn - 1, yn) or isavailable(xn, yn - 1) or isavailable(xn, yn + 1):
            result += 1
        if isavailable(xn + 1, yn):
            queue.append([xn + 1, yn])
        if isavailable(xn - 1, yn):
            queue.append([xn - 1, yn])
        if isavailable(xn, yn + 1):
            queue.append([xn, yn + 1])
        if isavailable(xn, yn - 1):
            queue.append([xn, yn - 1])

def bfs_dongbin(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            xn = x + dx[i]
            yn = y + dy[i]
            if xn < 0 or xn >= N or yn < 0 or yn >= M:
                continue
            if graph[xn][yn] == 0:
                continue
            if graph[xn][yn] == 1:
                graph[xn][yn] = graph[x][y] + 1
                queue.append((xn, yn))
    return graph[N-1][M-1]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
        




N, M = list(map(int, input().split()))

# print(N, M)

graph = []
for i in range(5):
    graph.append(list(map(int, input())))

start_time = time.time()
print(bfs_dongbin(0, 0))
print(time.time() - start_time)

start_time = time.time()
print(bfs(0, 0))
print(time.time() - start_time)

# print(graph)