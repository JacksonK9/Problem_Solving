import sys

sys.setrecursionlimit(100000000)

def pow(a, b):
    if b % 2 == 1:
        return a * pow(a ** 2, b // 2)
    else:
        return pow(a ** 2, b // 2)

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(pow(a, b) % 10)