# 블랙잭 문제
from itertools import combinations

N, M = list(map(int, input().split()))

data = tuple(map(int, input().split()))

diff = 300000
best = 0

result = list(combinations(data, 3))


for i in result:
    summation = sum(i)
    if summation == M:
        best = summation
        break
    elif summation > M:
        continue

    elif M - summation < diff:
        diff = M - summation
        best = summation

print(best)