N = int(input())

if N >= 23:
    hour = 3
elif N >= 13:
    hour = 2
elif N >= 3:
    hour = 1
else:
    hour = 0
    

minute = 15 # 3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53
second = 15 # 3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53

all_number_of_cases = (N + 1) * 60 * 60
except_cases = (N + 1 - hour) * 45 * 45

print(all_number_of_cases - except_cases)