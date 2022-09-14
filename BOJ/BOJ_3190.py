"""BOJ 3190 Problem."""

import sys

input = sys.stdin.readline

N = int(input())

K = int(input()) # 사과 개수

apples = []

for _ in range(K):
    r, c = map(int, input().split())
    apples.append((r - 1, c - 1))
    
L = int(input())

changes = []

for _ in range(L):
    X, C = input().strip().split()
    changes.append((int(X), C))

snake = [0, 0, 0] # 오른쪽 0, 위 1, 왼 2, 아래 3

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
time = 0

snakes = [(snake[0], snake[1])]
while True:
    time += 1

    snake[0] += dx[snake[2]]
    snake[1] += dy[snake[2]]
    
    if (snake[0], snake[1]) in apples:
        apples.pop(apples.index((snake[0], snake[1])))
        snakes.append((snake[0], snake[1]))
    else:
        snakes.append((snake[0], snake[1]))
        if len(snakes) != len(set(snakes)) or not 0 <= snake[0] < N or not 0 <= snake[1] < N:
            break
        snakes.pop(0)
        
    if len(snakes) != len(set(snakes)) or not 0 <= snake[0] < N or not 0 <= snake[1] < N:
        break
    
    for change in changes:
        if time < change[0]:
            break
        elif time == change[0]:
            if change[1] == 'L':
                snake[2] += 1
                if snake[2] == 4:
                    snake[2] = 0
            else:
                snake[2] -= 1
                if snake[2] == -1:
                    snake[2] = 3
            
print(time)
