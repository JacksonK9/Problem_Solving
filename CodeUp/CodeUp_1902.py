# 1에서 n까지 역순으로 출력하기
# 정수 n부터 1까지 출력하는 재귀함수를 설계하시오
# for, while, goto 사용 금지

N = int(input())

def print_recursive(_i, _N):
    if _i == 1:
        print(1)
        return
    else:
        print(_i)
        print_recursive(_i - 1, _N)

print_recursive(N, N)