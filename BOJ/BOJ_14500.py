"""BOJ 14500 Problem."""

import sys

input = sys.stdin.readline
N, M = map(int, input().split())

technomino = [
                [(0, 0), (1, 0), (2, 0), (3, 0)],
                [(0, 0), (0, 1), (0, 2), (0, 3)],
                [(0, 0), (1, 0), (0, 1), (1, 1)],
                [(0, 0), (1, 0), (2, 0), (2, 1)],
                [(0, 0), (1, 0), (2, 0), (2, -1)],
                [(0, 0), (-1, 0), (-2, 0), (-2, -1)],
                [(0, 0), (-1, 0), (-2, 0), (-2, 1)],
                [(0, 0), (0, 1), (0, 2), (1, 2)],
                [(0, 0), (0, 1), (0, 2), (-1, 2)],
                [(0, 0), (0, -1), (0, -2), (-1, -2)],
                [(0, 0), (0, -1), (0, -2), (1, -2)],
                [(0, 0), (0, 1), (1, 1), (1, 2)],
                [(0, 0), (0, 1), (-1, 1), (-1, 2)],
                [(0, 0), (1, 0), (1, 1), (2, 1)],
                [(0, 0), (1, 0), (1, -1), (2, -1)],
                [(0, 0), (0, -1), (0, 1), (1, 0)],
                [(0, 0), (-1, 0), (1, 0), (0, -1)],
                [(0, 0), (0, -1), (0, 1), (-1, 0)],
                [(0, 0), (1, 0), (0, 1), (-1, 0)]
              ]

val_map = []

for i in range(N):
    val_map.append(list(map(int, input().split())))

max_value = 0
for i in range(N):
    for j in range(M):
        for block in technomino:
            tmp_value = 0
            for r, c in block:
                if 0 <= (i + r) < N and 0 <= (j + c) < M:
                    tmp_value += val_map[i + r][j + c]
                else:
                    break
            if tmp_value > max_value:
                max_value = tmp_value

print(max_value)
