from collections import deque

def bfs(x, y, _graph):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if _graph[nx][ny] == 0:
                continue
            
            if _graph[nx][ny] == 1 and not (nx == 0 and ny == 0):
                _graph[nx][ny] = _graph[x][y] + 1
                queue.append((nx, ny))

        if _graph[-1][-1] != 1:
            break

    print(_graph[-1][-1])

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

bfs(0, 0, graph)