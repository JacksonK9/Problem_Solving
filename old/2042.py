import sys
input = sys.stdin.readline
# 데이터 개수 n, 변경 횟수 m, 구간 합 계산 횟수 k
n, m, k = map(int, input().split())
arr = [0] * (n + 1) # 1번부터 사용 예정
BIT = [0] * (n + 1) # 1번부터 사용 예정

def prefix_sum(i):
    result = 0
    while i > 0:
        result += BIT[i]
        i -= (i & -i)
    return result

def update(i, difference): # 기존 값과의 차이를 입력
    while i <= n:
        BIT[i] += difference
        i += (i & -i)

def interval_sum(left, right):
    return prefix_sum(right) - prefix_sum(left - 1)

for i in range(1, n + 1):
    x = int(input())
    arr[i] = x # 값을 데이터에 넣은 후
    update(i, x) # BIT도 업데이트

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1: # 값을 변경할 때
        update(b, c - arr[b])
        arr[b] = c
    elif a == 2: # 구간 합을 계산할 때
        print(interval_sum(b, c))
    else: # 입력 오류
        print("입력이 잘못되었습니다, 1 또는 2를 넣어야합니다.")
