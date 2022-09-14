chess_normal = [1, 1, 2, 2, 2, 8]

chess_dh = list(map(int, input().split()))

for i, j in zip(chess_normal, chess_dh):
    print(i - j, end=' ')