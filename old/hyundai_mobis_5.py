from itertools import combinations
N = int(input())

drones = list(map(int, input().split()))

result_set = list()

tmp_list = list()

for i in range(N):
    tmp_list.append(drones[i])
    if len(tmp_list) != len(set(tmp_list)):
        tmp_list.pop()
        tmp_result = []
        for j in range(0, len(tmp_list)): # 시작 index
            for k in range(1, len(tmp_list) + 1): # 길이
                if j + k > len(tmp_list):
                    break
                else:
                    tmp_result.append(sorted(tmp_list[j:j+k]))
        print(tmp_result)
        for j in tmp_result:
            if not j in result_set:
                result_set.append(j)
        tmp_list = [drones[i]]
    if i == N - 1:
        tmp_result = []
        for j in range(0, len(tmp_list)):
            for k in range(1, len(tmp_list) + 1):
                if j + k > len(tmp_list):
                    break
                else:
                    tmp_result.append(sorted(tmp_list[j:j+k]))
        # print(tmp_result)
        for j in tmp_result:
            if not j in result_set:
                result_set.append(j)
        tmp_list = [drones[i]]
print(len(result_set))