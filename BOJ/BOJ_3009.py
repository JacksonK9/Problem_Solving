points = []

for _ in range(3):
    points.append(list(map(int, input().split())))
    
x1, y1 = points[0]
x1_cnt = 1
y1_cnt = 1
x2_cnt = 0
y2_cnt = 0
for x, y in points[1:]:
    if x1 == x:
        x1_cnt += 1
    else:
        x2 = x
        x2_cnt += 1
        
    if y1 == y:
        y1_cnt += 1
    else:
        y2 = y
        y2_cnt += 1
        
if x1_cnt == 2:
    tmp_x = x2

if x2_cnt == 2:
    tmp_x = x1
    
if y1_cnt == 2:
    tmp_y = y2
    
if y2_cnt == 2:
    tmp_y = y1
    
print(tmp_x, tmp_y)