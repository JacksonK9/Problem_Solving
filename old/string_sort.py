data = list(input())
print(data)
data.sort()

sum = 0
print(ord('1'))
print(ord('A'))

for idx, i in enumerate(data):
    if ord(i) >= 65:
        first_idx = idx
        break
    
    sum += int(i)
print(first_idx)
new_string = "".join(data[first_idx:])

print(new_string, end="")
print(sum)

