arr = [None]
arr += (list(map(int, input().split())))
print(arr)
prefix_sum = [0] * (len(arr))
for i in range(1, len(arr)):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

left, right = map(int, input().split())\

print(prefix_sum[right] - prefix_sum[left - 1])