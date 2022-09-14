# # 덩치 문제

# T = int(input())

# data = []
# for i in range(T):
#     data.append(tuple(map(int, input().split())))

# rank = [0 for _ in range(T)]
# weight = sorted(data, key=lambda x:x[0], reverse=True)
# height = sorted(data, key=lambda x:x[1], reverse=True)

# # print(weight)
# # print(height)

# now = 1
# cnt = 0
# for i in range(T):
#     if weight[i] == height[i] and cnt == 0:
#         for idx, people in enumerate(data):
#             if people == weight[i]:
#                 rank[idx] = now
#                 now = now + 1
#                 break
#     elif cnt == 0:
#         for idx, people in enumerate(data):
#             if people == weight[i]:
#                 rank[idx] = now
#                 cnt += 1
#                 break
#     elif weight[i] != height[i] and cnt != 0:
#         for idx, people in enumerate(data):
#             if people == weight[i]:
#                 rank[idx] = now
#                 cnt += 1
#                 now += cnt
#                 cnt = 0
#                 break
#     else:
#         for idx, people in enumerate(data):
#             if people == weight[i]:
#                 rank[idx] = now
#                 cnt += 1
#                 break

# print(rank)


T = int(input())

data = []
for i in range(T):
    data.append(tuple(map(int, input().split())))

rank = []
for i in range(len(data)):
    cnt = 0
    for j in range(len(data)):
        if i == j:
            continue
        else:
            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                cnt += 1
            
    rank.append(cnt+1)

print(" ".join(map(str, rank)))