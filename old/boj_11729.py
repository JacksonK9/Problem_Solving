# 하노이 타워 문제

def hanoi(_N, _start, _target, _aux):
    if _N == 1:
        print(_start, _target)
    else:
        hanoi(_N-1, _start, _aux, _target)
        print(_start, _target)
        hanoi(_N-1, _aux, _target, _start)


N = int(input())

print(2 ** N - 1)
hanoi(N, 1, 3, 2)

