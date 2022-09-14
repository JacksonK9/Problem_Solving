import sys

input = sys.stdin.readline

result = 0
max_val = 0

for _ in range(4):
    o, i = map(int, input().split())
    result += i
    result -= o
    if result > max_val:
        max_val = result
    
print(max_val)