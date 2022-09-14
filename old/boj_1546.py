# 자기 점수 중 최댓값 고르기 --> M
# 모든 점수를 점수 / M * 100으로 변경
# 요렇게 변경했을 때의 새로운 평균 점수 구하기

# 과목 수 N 입력
# N개의 점수 입력

N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

for i in range(N):
    scores[i] = scores[i] / max_score * 100

print(sum(scores)/N)