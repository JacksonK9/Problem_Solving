import string

N = list(input())

cnt = []
for i in string.digits:
    cnt.append(N.count(i))
    
cnt[6] += cnt[9]
cnt[9] = 0
if cnt[6] % 2 == 1:
    cnt[6] = (cnt[6] + 1) // 2
else:
    cnt[6] = (cnt[6] // 2)
print(max(cnt))
