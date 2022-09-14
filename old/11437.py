import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5)) # 재귀함수의 호출 가능 횟수를 늘리는 부분
N = int(input())

parent = [0] * (N + 1) # 각 Node의 부모 정보를 담는 리스트
d = [0] * (N + 1) # 각 Node의 깊이
c = [0] * (N + 1) # 각 Node의 깊이가 계산 되었는 지 여부 (DFS 방문 여부 저장용)
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1): # Tree의 Edge 개수는 N - 1이므로
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth): # 깊이 계산용 dfs
    c[x] = True
    d[x] = depth
    for connected in graph[x]:
        if c[connected] == True:
            continue
        parent[connected] = x # 이미 조사를 했다는 얘기는 부모라는 의미이므로 남아있으면 자식
        dfs(connected, depth + 1) # 남아있는 자식은 depth + 1해서 호출

def lca(a, b): # a와 b의 공통 조상을 찾는 알고리즘
    if d[b] > d[a]: # a가 더 깊거나 같게 변경
        a, b = b, a
    
    while d[a] != d[b]: # a와 b의 깊이가 같을 때까지 반복
        a = parent[a] # a를 거슬러 올라가기
    
    while a != b: # 두 Node의 부모가 같을 때까지 반복
        a = parent[a] # a 거슬러 올라가기
        b = parent[b] # b 거슬러 올라가기
    
    return a

dfs(1, 0) # Root Node는 1번이며, 이는 깊이가 0

M = int(input()) # 입력할 개수를 M에 받을 예정

for i in range(M): # M개를 받아서, lca 함수 호출
    a, b = map(int, input().split())
    print(lca(a, b))