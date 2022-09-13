K = int(input())


num_lst = []
for _ in range(K):
    tmp = int(input())
    if tmp == 0:
        num_lst.pop()
    else:
        num_lst.append(tmp)
        
print(sum(num_lst))