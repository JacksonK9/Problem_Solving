# 두 가지 행사 
# 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우, 할인된 정액 가격으로 제공
# 초밥의 종류 하나가 쓰인 쿠폰을 발행, 1번 행사에 참가할 경우 쿠폰에 적혀진 초밥 하나를 추가로 무료 제공, 벨트 위에 없을 경우, 요리사가 직접 만들어서 제공
# 벨트의 상태, 초밥의 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호가 주어졌을 때, 먹을 수 있는 초밥 가짓수의 최대값을 구하는 프로그램
# N, d, k, c = map(int, input().split())
# belt = []
# for _ in range(N):
#     belt.append(int(input()))

# for i in range(k - 1):
#     belt.append(belt[i])

# max = 0
# for i in range(N):
#     tmp_belt = set(belt[i:i+k])
#     if c in tmp_belt:
#         tmp_max = len(tmp_belt)
#     else:
#         tmp_max = len(tmp_belt) + 1
#     if tmp_max > max:
#         max = tmp_max
# print(max)


old_string = "Hello World"
# old_string[0] = "J" #  Error happen

new_string = list(old_string)
new_string[0] = "J"
new_string = ''.join(new_string)

another_string = ' '.join(new_string)

print(old_string) # Hello World
print(new_string) # Jello World
print(another_string) 