import sys

input = sys.stdin.readline

N, B = map(int, input().split()) # 컴퓨터의 대수, 업그레이드 예산

PCs = list(map(int, input().split())) # 각 PC의 성능

left = 1 
right = 2000000000

while (left + 1) < right: # 무한 루프에 빠지지 않도록, 1보다 적게 차이나면 멈추도록 설정
    cost = 0
    center = (left + right) // 2 # 무조건 버려짐
    for i in PCs:
        if i < center:
            cost += (center - i) ** 2
            if cost > B:
                right = center - 1
                break
    else:
        left = center

best_PC = 0
for center in range(left, right + 1): 
    # left or right 중, 최적이 어떤 것인지 한 번 더 확인
    cost = 0
    for i in PCs:
        if i < center:
            cost += (center - i) ** 2
            
    if cost <= B:
        best_PC = center

print(best_PC)
