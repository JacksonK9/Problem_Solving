import string

S = list(input())

result = []
for i in string.ascii_lowercase:
    result.append(S.count(i))
    
print(*result)