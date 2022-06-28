# 입체기동장치 생산 공장ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# 입체기동장치의 식별번호 (1~100) 그리고 남은 가스량 (0~10000)을 함께 관리
# 미카사가 대신 해결해줄 예정 갓 미카사...
# 식별번호가 지정되면, 가스 보유량은 정렬되더라도 변경되면 안된다고 합니다.
# =====================입력==============================
# 첫째 줄에 입체기동장치 개수 N이 입력 (1 <= N <= 100)
# 둘째 줄부터 N + 1째 줄까지 각 줄에 입체기동장치의 식별번호 A와 가스 보유량 B가 주어진다.
# A는 중복 될 수 없지만 B는 중복될 수 있다. (1 <= A <= 100), (0 <= B <= 10,000)
'''
3
2 10
3 20
1 30
'''
# =====================출력==============================
# 첫째 줄부터 N번째 줄까지 각 줄에 식별번호를 오름차순으로 정렬해 가스 보유량과 같이 출력한다.
'''
1 30
2 10
3 20
'''
# # 방법 1. 그냥 파이썬의 특정을 이용하여, 두 값을 리스트로 묶어서 정렬시키는 방법을 사용한다.
# N = int(input())
# Maneuver_Gear = []
# for _ in range(N):
#     Maneuver_Gear.append(list(map(int, input().split())))

# Result = sorted(Maneuver_Gear, key=lambda x: x[0])

# for i in Result:
#     print(i[0], i[1])

# 방법 2. 클래스 이용하기...?

class Maneuver_Gear():
    def __init__(self, _serial_num, _gas):
        self.serial_num = _serial_num
        self.gas = _gas

N = int(input())

Gears = []
for _ in range(N):
    A, B = map(int, input().split())
    Gears.append(Maneuver_Gear(A, B))
Result = sorted(Gears, key=lambda x: x.serial_num)
for i in Result:
    print(i.serial_num, i.gas)