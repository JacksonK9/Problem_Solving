r, c = list(input())

move_plans = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
position = [int(c), ord(r)-96]
cnt = 0
for plan in move_plans:
    tmp_x = position[0] + plan[0]
    tmp_y = position[1] + plan[1]
    if 1 <= tmp_x <= 8 and 1 <= tmp_y <= 8 :
        cnt += 1
print(cnt)

