N = int(input())

for i in range(1, N + 1):
    num_star = 2 * i - 1
    num_blank = 2 * N - 1 - num_star
    
    print(" " * (num_blank // 2) + "*" * num_star)