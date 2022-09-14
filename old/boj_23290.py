
M, S = map(int, input().split())

grid = [[-1, -1, -1, -1, -1], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0]] # -1은 이동할 수 없는 영역
fish_grid = [[-1, -1, -1, -1, -1], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, 0, 0, 0, 0]] # -1은 이동할 수 없는 영역

directions = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

shark_directions = [[0, 0], [-1, 0], [0, -1], [1, 0], [0, 1]]

# print(grid)

class fish():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction # 1이 왼쪽이며, 8까지 시계방향, 3은 위쪽, 5는 오른쪽, 7은 아래쪽을 의미
        fish_grid[x][y] += 1

    def update_direction(self):
        self.direction -= 1
        if self.direction == 0:
            self.direction = 8

    def update_position(self):
        fish_grid[self.x][self.y] -= 1
        self.x += directions[self.direction][0]
        self.y += directions[self.direction][1]
        fish_grid[self.x][self.y] += 1

class shark():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def process1():
    return [fish for fish in fishes]

def process2():
    for fish in fishes:
        cnt = 0
        while cnt < 8:
            tmp_x = fish.x + directions[fish.direction][0]
            tmp_y = fish.y + directions[fish.direction][1]
            if tmp_x > 4 or tmp_y > 4 or tmp_x < 1 or tmp_y < 1:
                cnt += 1
                fish.update_direction()
                continue

            elif grid[fish.x + directions[fish.direction][0]][fish.y + directions[fish.direction][1]] == 0:
                fish.update_position()
            else:
                cnt += 1
                fish.update_direction()

def process3():
    best = 0
    best_case = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                tmp_x1 = magic_shark.x + shark_directions[i][0]
                tmp_y1 = magic_shark.y + shark_directions[i][1]
                tmp_x2 = tmp_x1 + shark_directions[j][0]
                tmp_y2 = tmp_y1 + shark_directions[j][1]
                tmp_x3 = tmp_x2 + shark_directions[k][0]
                tmp_y3 = tmp_y2 + shark_directions[k][1]
                if tmp_x1 > 4 or tmp_y1 > 4 or tmp_x2 > 4 or tmp_y2 > 4 or tmp_x3 > 4 or tmp_y3 > 4 or tmp_x1 < 1 or tmp_y1 < 1 or tmp_x2 < 1 or tmp_y2 < 1 or tmp_x3 < 1 or tmp_y3 < 1:
                    continue
                tmp_result = fish_grid[tmp_x1][tmp_y1] + fish_grid[tmp_x2][tmp_y2] + fish_grid[tmp_x3][tmp_y3]
                if tmp_result > best:
                    best = tmp_result
                    best_case = [[i, j, k]]
                elif tmp_result == best:
                    best_case.append([i, j, k])
                else:
                    pass
    i, j, k = best_case[0]
    tmp_x1 = magic_shark.x + shark_directions[i][0]
    tmp_y1 = magic_shark.y + shark_directions[i][1]
    tmp_x2 = tmp_x1 + shark_directions[j][0]
    tmp_y2 = tmp_y1 + shark_directions[j][1]
    tmp_x3 = tmp_x2 + shark_directions[k][0]
    tmp_y3 = tmp_y2 + shark_directions[k][1]
    if fish_grid[tmp_x1][tmp_y1] != 0:
        fish_grid[tmp_x1][tmp_y1] = 0
        grid[tmp_x1][tmp_y1] = 2
        for i in range(len(fishes)):
            if fishes[i].x == tmp_x1 and fish[i].y == tmp_y1:
                fishes.pop(i)

    if fish_grid[tmp_x2][tmp_y2] != 0:
        fish_grid[tmp_x2][tmp_y2] = 0
        grid[tmp_x2][tmp_y2] = 2
        for i in range(len(fishes)):
            if fishes[i].x == tmp_x1 and fish[i].y == tmp_y1:
                fishes.pop(i)

    if fish_grid[tmp_x3][tmp_y3] != 0:
        fish_grid[tmp_x3][tmp_y3] = 0
        grid[tmp_x3][tmp_y3] = 2
        for i in range(len(fishes)):
            if fishes[i].x == tmp_x1 and fish[i].y == tmp_y1:
                fishes.pop(i)
    
    grid[magic_shark.x][magic_shark.y] = 0
    magic_shark.x = tmp_x3
    magic_shark.y = tmp_y3
    grid[magic_shark.x][magic_shark.y] = 5

    
    return best_case[0]

def process4():
    for i in range(1, 5):
        for j in range(1, 5):
            if grid[i][j] > 0:
                grid[i][j] -= 1

def process5(_saved_fishes):
    for fish in _saved_fishes:
        fish_grid[fish.x][fish.y] += 1
    fishes.extend(_saved_fishes)





fishes = []
for _ in range(M):
    x, y, direction = map(int, input().split())
    fishes.append(fish(x, y, direction))

# print(fish_grid)

x, y = map(int, input().split())
magic_shark = shark(x, y)
grid[x][y] = 5 # 상어의 위치는 5

for _ in range(S):
    saved_fishes = process1()
    process2()
    process3()
    process4()
    process5(saved_fishes)

print(fish_grid)
# print(sum(sum(fish_grid[1:5][1:5])))