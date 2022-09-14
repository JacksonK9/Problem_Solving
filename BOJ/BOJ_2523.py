N = int(input())

for i in range(1, N + 1):
    tmp_str = '*' * i
    print(tmp_str)
    
for i in range(N - 1, 0, -1):
    tmp_str = '*' * i
    print(tmp_str)