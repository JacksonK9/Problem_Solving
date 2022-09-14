N = int(input())

for i in range(1, N + 1):
    tmp_str = "*" * (2 * i - 1)
    new_str = tmp_str.center(2 * N - 1)
    print(new_str.rstrip())
    
for i in range(N - 1, 0, -1):
    tmp_str = "*" * (2 * i - 1)
    new_str = tmp_str.center(2 * N - 1)
    print(new_str.rstrip())