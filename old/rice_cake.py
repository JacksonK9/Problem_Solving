## 떡볶이 떡 문제
N, M = list(map(int, input().split()))

data = list(map(int, input().split()))

start = 0
end = max(data)
target = None

while (start <= end):
    total = 0
    middle = (start + end) // 2
    # print(middle)
    # print([i - data[middle] for i in data[middle:]])
    for x in data:
        if x > middle:
            total += x - middle
    # if total >= M:
    #     target = middle
    #     start = middle + 1
    #     # break
    # elif total < M:
    #     end = middle - 1
    if total < M:
        end = middle - 1
    else:
        target = middle
        start = middle + 1
    
print(target)