# 영화감독 숌

N = int(input())

cnt = 0
start = 666
result = 0
while True:
    test_data = str(start)
    if '666' in test_data:
        cnt += 1
        result = start
    
    if cnt == N:
        print(result)
        break
    start += 1