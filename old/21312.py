numbers = list(map(int, input().split()))

isOdd = [False] * 3

for i in range(3):
    if numbers[i] %2 == 1:
        isOdd[i] = True
result = 1
if True in isOdd:
    for i in range(3):
        if isOdd[i] == True:
            result *= numbers[i]

else:
    for i in range(3):
        result *= numbers[i]

print(result)