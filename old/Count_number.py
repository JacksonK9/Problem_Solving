# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

def count(arr, left, right):
    left_idx = bisect_left(arr, left)
    right_idx = bisect_right(arr, right)

    if right_idx - left_idx == 0:
        return -1
    return right_idx  - left_idx


N, x = list(map(int, input().split()))
arr = list(map(int, input().split()))

print(count(arr, x, x))