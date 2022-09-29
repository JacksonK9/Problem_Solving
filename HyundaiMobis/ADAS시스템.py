# -*- coding: utf-8 -*-
import sys
import heapq

input = sys.stdin.readline

W, H = map(int, input().split())
virtual_env = [input().strip() for _ in range(W)]

def is_valid_coordinate(x, y):
    if 0 <= x < W and 0 <= y < H:
        return True
    return False

def find_S(virtual_env):
    for x, value in enumerate(virtual_env):
        y = value.find('S')
        if y == -1:
            continue
        return (x, y)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
hq = []
S_x, S_y = find_S(virtual_env)
heapq.heappush(hq, (0, S_x, S_y))
visited = set()
visited.add(S_x * H + S_y)

def calc_point(x, y):
    tmp_score = 0
    if virtual_env[x][y] == 'S' or virtual_env[x][y] == 'E':
        return 0
    if virtual_env[x][y] == 'P':
        tmp_score = -3
    for r in range(x - 1, x + 2):
        for c in range(y - 1, y + 2):
            if (r == x and c == y) or not is_valid_coordinate(r, c):
                continue
            if virtual_env[r][c] == 'P':
                tmp_score += 1
    return tmp_score
            

danger_point = 0
while hq:
    _, now_x, now_y = heapq.heappop(hq)
    if virtual_env[now_x][now_y] == 'E':
        break
    danger_point += calc_point(now_x, now_y)
    
    for direction in range(4):
        tmp_x = now_x + dx[direction]
        tmp_y = now_y + dy[direction]
        if (tmp_x * H + tmp_y) in visited:
            continue
        if not is_valid_coordinate(tmp_x, tmp_y):
            continue
        if virtual_env[tmp_x][tmp_y] == 'E':
            heapq.heappush(hq, (0, tmp_x, tmp_y))
        elif virtual_env[tmp_x][tmp_y] == 'P':
            heapq.heappush(hq, (1, tmp_x, tmp_y))
        elif virtual_env[tmp_x][tmp_y] == '0':
            heapq.heappush(hq, (2, tmp_x, tmp_y))
        visited.add(tmp_x * H + tmp_y)

print(danger_point)
