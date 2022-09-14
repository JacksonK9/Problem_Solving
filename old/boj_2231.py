# 분해합 문제

N = int(input())

isFind = False
for i in range(2, N):
    result = i
    data = list(str(i))
    # print(data)
    result = result + sum(map(int, data))
    # print(result)
    if result == N:
        isFind = True
        print(i)
        break
if not isFind:
    print(0)
