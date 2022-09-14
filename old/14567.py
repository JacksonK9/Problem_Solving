from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

Edges = [[] for _ in range(N + 1)]

indegree = [0] * (N + 1)

for i in range(M):
    start, target = map(int, input().split())
    Edges[start].append(target)
    indegree[target] += 1

q = deque()
result = [0] * (N + 1)

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        result[i] = 1

while q:
    now = q.popleft()
    for i in Edges[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
            result[i] = result[now] + 1


for i in range(1, len(result)):
    print(result[i], end=' ')
