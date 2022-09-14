for _ in range(3):
    tmp = list(map(int, input().split()))
    cnt_O = tmp.count(0)
    cnt_1 = tmp.count(1)
    if cnt_1 == 4:
        print('E')
    else:
        print(chr(cnt_O + 64))
