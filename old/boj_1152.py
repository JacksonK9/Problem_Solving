# 영어 대소문자와 공백으로 이루어진 문자열
# 단어의 개수를 추가는 프로그램
# 단어는 공백 하나로 구분되며, 공백이 연속해서 나오는 경우는 없음
# 문자열은 공백으로 시작하거나 끝날 수 있음

input_str = list(input().strip().split())

print(len(input_str))

# 한줄컷도 가능
# print(len(list(input().strip().split())))