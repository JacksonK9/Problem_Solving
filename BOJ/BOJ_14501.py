# 퇴사 문제
# N + 1번째 되는 날에 퇴사, N일간 최대한 열심히 근무 (최대한 많은 상담)
# 각 상담은 상담에 필요한 기간과 이에 대한 금액으로 구성
# 퇴사하기 전까지 최대한의 비용을 얻을 수 있는 최대 수익 계산

N = int(input())

interview = [[]]

for _ in range(N):
    interview.append(list(map(int, input().split())))

## i일에 일을 시작하면, i + T - 1까지는 일을 못함
## i + T - 1 > N이면, 최종까지 완료할 수 없음
## i + T - 1 <= N이면, 금액을 받을 수 있음
## N일까지의 최대 비용 = max(N - 1일까지의 최대 비용, N - 1일의 비용 + N일에 종료되는 비용)
## 1일의 최대 비용 = 0, 2일의 최대 비용 = 1일의 최대 비용 + 2일에 종

costs = [[] for _ in range(N + 2)] # 최대 N + 1일의 비용까지 계산 가능하도록
costs[1].append(0)
for i in range(1, N + 1): # 최대 N일까지를 계산
    if len(costs[i - 1]) != 0:
        costs[i].append(max(costs[i - 1]))
    T, P = interview[i]
    if i + T > N + 1: # 현재 날짜에서 T를 더한 날이 되면 비용 계산이 끝나며, 그 날이 N + 1일 이후이면 계산할 필요 없음
        continue
    if len(costs[i]) == 0:
        costs[i + T].append(P)
    else:
        costs[i + T].append(max(costs[i]) + P)

if len(costs[-2]) != 0:
    costs[-1].append(max(costs[-2]))

print(max(costs[-1]))
