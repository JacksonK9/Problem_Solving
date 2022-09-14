N = int(input())

for i in range(1, N + 1):
    blank_cnt = N - i
    tmp_str = "*" * i + " " * blank_cnt
    tmp = list(tmp_str)
    tmp.reverse()
    new_str = tmp_str + ''.join(tmp)
    print(new_str)

for i in range(N - 1, 0, -1):
    blank_cnt = N - i
    tmp_str = "*" * i + " " * blank_cnt
    tmp = list(tmp_str)
    tmp.reverse()
    new_str = tmp_str + ''.join(tmp)
    print(new_str)