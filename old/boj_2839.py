# 설탕 배달 문제

# 1. Greedy Algorithm으로 풀기
# 5키로로 나누어지는 경우는 5키로로 나누어주는 것이 가장 적게 들고 갈 수 있는 방법
# 5키로로 나누어지지 않는 경우는 5키로로 나누어질 때까지 3키로씩 빼는 방법을 적용
# N = int(input())

# result = 0
# while N % 5 != 0:
#     result += 1
#     N -= 3
#     if N < 0:
#         result = -1
#         break

# if result == -1:
#     print(result)
# else:
#     result += N // 5
#     print(result)

# 2. Dynamic Programming으로 풀기
# Bottom Up 방식으로 최소 개수가 몇 개인지 적어가며 진행
N = int(input())

dp = [0] * (5001)
dp[1] = -1
dp[2] = -1
dp[3] = 1
dp[4] = -1
dp[5] = 1

for i in range(6, N + 1):
    if dp[i - 3] == -1 and dp[i - 5] == -1:
        dp[i] = -1
    elif dp[i - 3] == -1:
        dp[i] = dp[i - 5] + 1
    elif dp[i - 5] == -1:
        dp[i] = dp[i - 3] + 1
    else:
        dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)

print(dp[N])

