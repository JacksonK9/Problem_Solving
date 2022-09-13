ascend = [1, 2, 3, 4, 5, 6, 7, 8]
descend = [8, 7, 6, 5, 4, 3, 2, 1]

melody = list(map(int, input().split()))

if melody == ascend:
    print("ascending")

elif melody == descend:
    print("descending")

else:
    print("mixed")