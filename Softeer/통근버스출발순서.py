import sys

input = sys.stdin.readline

N = int(input())

buses = list(map(int, input().split()))

arr = [[0] * (N + 1) for _ in range(N + 1)]

for j in range(N - 1, -1, -1):
    for X in range(1, N + 1):
        if buses[j] < X:
            arr[X][j] = arr[X][j + 1] + 1
        else:
            arr[X][j] = arr[X][j + 1]

result = 0
for i in range(N):
    for j in range(i, N):
        if buses[i] < buses[j]:
            result += arr[buses[i]][j]
            
print(result)
