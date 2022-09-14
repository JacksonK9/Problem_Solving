"""Code for BOJ 15686 Problem."""

from itertools import combinations
N, M = map(int, input().split())

map_orig = []

chicken = []
for i in range(N):
    tmp = list(map(int, input().split()))
    while tmp.count(2) != 0:
        idx = tmp.index(2)
        chicken.append((i, idx))
        tmp[idx] = 0
    map_orig.append(tmp)

# 0은 빈칸, 1은 집, 2는 치킨집
# 일단... 1. 치킨 집의 위치를 구해온다.
# 2. 각 치킨 집 중 M개를 선택한다.
# 3. 선택된 M개의 치킨 집과 각 집 사이의 거리를 계산하여, 최소 값을 더한다.

chicken_select = combinations(chicken, M)

min_dist = float('inf')

for chicken_lst in chicken_select:
    min_dist_tmp = 0
    for i in range(N):
        for j in range(N):
            if map_orig[i][j] == 1:
                tmp_dist = float('inf')
                for r, c in chicken_lst:
                    calc_dist = abs(r - i) + abs(c - j)
                    if tmp_dist > calc_dist:
                        tmp_dist = calc_dist
                min_dist_tmp += tmp_dist
    if min_dist > min_dist_tmp:
        min_dist = min_dist_tmp

print(min_dist)
