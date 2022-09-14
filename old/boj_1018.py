# 체스판 다시 칠하기

M, N = list(map(int, input().split()))

white_chess_board = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
black_chess_board = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

# print(white_chess_board)
# print(black_chess_board)
data = []
for _ in range(M):
    data.append(list(input()))

min_val = 64
for i in range(0, M - 8 + 1):
    for j in range(0, N - 8 + 1):
        diff_black = 0
        diff_white = 0
        # chess_board = data[i:i+8][j:j+8]
        for k in range(8):
            for l in range(8):
                if data[i + k][j + l] != white_chess_board[k][l]:
                    diff_white += 1
                if data[i + k][j + l] != black_chess_board[k][l]:
                    diff_black += 1
        min_val = min(min_val, diff_white, diff_black)

print(min_val)
# print(data)