# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline
N = int(input())
str_lst = [input().strip() for _ in range(N)]
K = int(input())
match_lst = [input().strip() for _ in range(K)]

for match in match_lst:
    matched = dict()
    for i, case in enumerate(str_lst):
        if len(case) < len(match):
            continue
        if case.find(match) == 0:
            if case in matched:
                matched[case] += 1
            else:
                matched[case] = 1
    if len(matched.values()) == 0:
        print(0)
        continue
    max_cnt = max(list(matched.values()))
    max_values = []
    for key, val in matched.items():
        if val == max_cnt:
            max_values.append(key)
    max_values.sort()
    print(max_values[0], max_cnt)