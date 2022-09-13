N = int(input())

for i in range(N, 0, -1):
    num_star = 2 * i - 1
    num_blank = 2 * N - 1 - num_star
    
    print(" " * (num_blank // 2) + "*" * num_star)
for i in range(2, N + 1):
    num_star = 2 * i - 1
    num_blank = 2 * N - 1 - num_star
    
    print(" " * (num_blank // 2) + "*" * num_star)