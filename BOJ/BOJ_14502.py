from itertools import permutations
from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

imap = []

for _ in range(N):
    imap.append(list(map(int, input().split())))

# 0은 빈칸, 1은 벽, 2는 바이러스, 벽이 없다면, 바이러스는 모든 빈칸으로 퍼져나갈 것
# 새로 세울 수 있는 벽의 개수는 3개, 꼭 3개를 세워야 함

q_initial = deque()

for i in range(N):
    for j in range(M):
        if imap[i][j] == 2:
            q_initial.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_num = 0
for i, j, k in permutations(range(N * M), 3):
    test_map = deepcopy(imap)
    if test_map[i // M][i % M] != 0 or test_map[j // M][j % M] != 0 or test_map[k // M][k % M] != 0:
        continue
    test_map[i // M][i % M] = 1
    test_map[j // M][j % M] = 1
    test_map[k // M][k % M] = 1
    
    q = deepcopy(q_initial)
    # visited = []
    while q:
        now = q.popleft()

        for m in range(4):
            tmp_x = now[0] + dx[m]
            tmp_y = now[1] + dy[m]
            if 0 <= tmp_x < N and 0 <= tmp_y < M:
                pass
            else:
                continue
            if test_map[tmp_x][tmp_y] == 0:
                # visited.append([tmp_x, tmp_y])
                test_map[tmp_x][tmp_y] = 2
                q.append((tmp_x, tmp_y))

    tmp = 0
    for l in test_map:
        tmp += l.count(0)
        
    if tmp > max_num:
        max_num = tmp
        
print(max_num)
        

    