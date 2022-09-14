"""BOJ 14503 Problem."""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

rr, rc, heading = map(int, input().split())

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

rotate = {0: 3, 1: 0, 2: 1, 3: 2}

room = []

for _ in range(N):
    room.append(list(map(int, input().split())))

clean_cnt = 0

while True:
    # 확인 후, 청소 진행
    # print("==========") # 0 북, 1 동, 2, 남, 3 서
    # print("direction {}".format(heading))
    # for i in room:
    #     print(*i)
    if room[rr][rc] == 0:
        room[rr][rc] = 2
        clean_cnt += 1
        continue

    for _ in range(4):
        tmp_x = rr + dx[rotate[heading]]
        tmp_y = rc + dy[rotate[heading]]
        if not 0 <= tmp_x < N or not 0 <= tmp_y < M:
            continue
        if room[tmp_x][tmp_y] == 0:
            rr = tmp_x
            rc = tmp_y
            heading = rotate[heading]
            break
        else:
            heading = rotate[heading]
    
    else:
        tmp_x = rr - dx[heading]
        tmp_y = rc - dy[heading]
        
        if not 0 <= tmp_x < N or not 0 <= tmp_y < M:
            break
        if room[tmp_x][tmp_y] == 1:
            break
        else:
            rr = tmp_x
            rc = tmp_y
        
print(clean_cnt)
