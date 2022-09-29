# -*- coding: utf-8 -*-
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

parking = [list(map(int, input().split())) for _ in range(N)]

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

area_score = 0

for i in range(N):
    for j in range(M):
        if parking[i][j] == 1:
            continue

        Q = deque([(i, j)])
        if parking[i][j] == 0:
            tmp_score = 1
        else:
            tmp_score = -2
        parking[i][j] = 1

        while Q:
            now_x, now_y = Q.popleft()
            for dx, dy in dxy:
                tmp_x = now_x + dx
                tmp_y = now_y + dy
                if not (0 <= tmp_x < N and 0 <= tmp_y < M):
                    continue
                if parking[tmp_x][tmp_y] != 1:
                    Q.append((tmp_x, tmp_y))
                    if parking[tmp_x][tmp_y] == 0:
                        tmp_score += 1
                    else:
                        tmp_score += -2
                    parking[tmp_x][tmp_y] = 1

        if area_score < tmp_score:
            area_score = tmp_score

print(area_score)
