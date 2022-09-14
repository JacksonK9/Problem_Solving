import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
LOG = 21 # 2^20 ~~ 1,000,000 # 최대 입력 크기가 약 100만 정도이므로

N = int(input())
parent = [[0] * LOG for _ in range(N + 1)] # 모든 Node에 대해 최대 21개까지의 부모를 저장할 수 있는 공간 할당
d = [0] * (N + 1) # 깊이 저장 공간
c = [0] * (N + 1) # 깊이 계산 여부 저장 공간
graph = [[] for _ in range(N + 1)] # Graph 정보 저장

for _ in range(N - 1): # Tree에서 N개의 Node에 대해 필요한 값은 N - 1개의 Edge
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for connected in graph[x]:
        if c[connected] == True:
            continue
        parent[connected][0] = x
        dfs(connected, depth + 1)

def set_parent():
    dfs(1, 0) # 1번이 Root Node이며, Depth가 0
    for i in range(1, LOG): # 최대 LOG개수까지 진행
        for j in range(1, N + 1): # 모든 Node에 대해 진행
            parent[j][i] = parent[parent[j][i - 1]][i - 1] # 2 ^ i의 부모는 2 ^ (i - 1) 부모의 2 ^ (i - 1)부모를 의미

def lca(a, b):
    if d[b] > d[a]: # 무조건 a가 더 깊거나 같게 설정
        a, b = b, a
    
    for i in range(LOG - 1, -1, -1): # 높은 수부터 확인해서
        if d[a] - d[b] >= 2 ** i: # 깊이 차이가 더 커지면
            a = parent[a][i] # 올라가기
    
    if a == b: # 혹시라도 두 값이 같아서, 이미 공통조상이면 반환
        return a
    
    for i in range(LOG - 1, -1, -1): # 높은 수부터 확인해서
        if parent[a][i] != parent[b][i]: # 두 수의 부모가 다르면
            a = parent[a][i] # 거슬러 올라가기
            b = parent[b][i] # 거슬러 올라가기
    
    return parent[a][0] # 다를때만 올라갔으므로, 하나 더 올라가야 공통 조상임

set_parent() # 먼저 부모를 설정

M = int(input()) # 계산할 횟수를 M에 저장

for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b)) # 입력받은 값의 공통 조상을 찾아서 출력