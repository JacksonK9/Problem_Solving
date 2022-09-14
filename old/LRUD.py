space_size = int(input())

move_plan = list(input().split())

pos = [0, 0]

def plan_to_vector(data):
    if data == 'R':
        return [0, 1]
    elif data == 'L':
        return [0, -1]
    elif data == 'U':
        return [-1, 0]
    elif data == 'D':
        return [1, 0]
    else:
        print("error")

def pos_plus_vector(pos, vector):
    print(pos)
    print(vector)
    temp = [0, 0]
    temp[0] = pos[0] + vector[0]
    temp[1] = pos[1] + vector[1]
    # temp = pos + vector
    if temp[0] < 0:
        temp[0] = 0
    if temp[0] >= space_size:
        temp[0] = space_size - 1
    if temp[1] < 0:
        temp[1] = 0
    if temp[1] >= space_size:
        temp[1] = space_size - 1
    print(temp)
    return temp

for i in move_plan:
    move_vector = plan_to_vector(i)
    # print(move_vector)
    pos = pos_plus_vector(pos, move_vector)
    print("---")

print(pos[0]+1, pos[1]+1)
