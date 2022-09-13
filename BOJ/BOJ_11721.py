word = input()

i = 0
while True:
    if (len(word) - i * 10) // 10 == 0:
        print(word[i * 10:])
        break
    else:
        print(word[i * 10 : (i + 1) * 10])
        i += 1