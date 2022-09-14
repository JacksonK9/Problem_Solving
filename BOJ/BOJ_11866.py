N, K = map(int, input().split())

tmp = list(range(1, N + 1))

new_lst = []
now = K - 1

while len(set(new_lst)) != N:
    now = now % len(tmp)
    new_lst.append(tmp.pop(now))
    now += (K - 1)
    
print("<", end='')
for i in new_lst:
    if i == new_lst[-1]:
        print(f'{i}', end='')
    else:
        print(f'{i},', end=' ')
print(">")
