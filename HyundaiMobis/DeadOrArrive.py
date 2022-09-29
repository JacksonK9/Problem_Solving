# -*- coding: utf-8 -*-
# Dead or Arrive 문제
import sys
input = sys.stdin.readline

N = int(input())

vehicles = []

for i in range(1, N + 1):
    v, w = map(int, input().split())
    vehicles.append((v, w, i))
    
s_vehicles = sorted(vehicles, key=lambda x: x[0])

speed_dict = dict()

for v, w, i in s_vehicles:
    if not v in speed_dict:
        speed_dict[v] = (w, i)
    elif w > speed_dict[v][0]:
        speed_dict[v] = (w, i)
    elif w == speed_dict[v][0]:
        if i > speed_dict[v][1]:
            speed_dict[v] = (w, i)
    
result = 0        
for (w, i) in speed_dict.values():
     result += i
     
print(result)
