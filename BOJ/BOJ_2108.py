from collections import Counter
import sys

input = sys.stdin.readline
N = int(input())

numbers = []

for _ in range(N):
    numbers.append(int(input()))

tmp = sum(numbers) / N

# int 변환 시, 양수는 모두 버림, 음수는 모두 올림 처리 됨
if tmp >= 0:
    if (tmp - int(tmp)) >= 0.5:
        print(int(tmp) + 1)
    else:
        print(int(tmp))
else:
    if abs(tmp - int(tmp)) >= 0.5:
        print((int(tmp) - 1))
    else:
        print((int(tmp))) 

numbers.sort()
print(numbers[int((N - 1) / 2)])

tmp = Counter(numbers).most_common(2)

if N == 1:
    print(numbers[0])
elif tmp[0][1] == tmp[1][1]:
    if tmp[0][0] < tmp[1][0]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(tmp[0][0])
    
print(numbers[-1] - numbers[0])
