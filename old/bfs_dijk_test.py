from queue import Queue, PriorityQueue
from collections import deque
import heapq
import time

def time_check_decorator(func):
    def decorated(*args, **kwargs):
        ref_time = time.time()
        func(*args, **kwargs)
        print(f'time : {time.time() - ref_time:.7f}s')
    return decorated

class normal_graph():
    def __init__(self, _node_num):
        self.edge = [[] for _ in range(_node_num + 1)]

    def add(self, _start, _end, _cost):
        self.edge[_start].append((_end, _cost))

    def neighbors(self, _position):
        result = []
        for end, cost in self.edge[_position]:
            result.append(end)
        return result

    def cost(self, _start, _next):
        for end, cost in self.edge[_start]:
            if end == _next:
                return cost

    def print_graph(self):
        print(self.edge)


graph = normal_graph(6)
graph.add(1, 2, 2)
graph.add(1, 3, 5)
graph.add(1, 4, 1)
graph.add(2, 3, 3)
graph.add(2, 4, 2)
graph.add(3, 2, 3)
graph.add(3, 6, 5)
graph.add(4, 5, 1)
graph.add(4, 3, 3)
graph.add(5, 3, 1)
graph.add(5, 6, 2)

graph.print_graph()


start = 1
goal = 6

# BFS Queue
@ time_check_decorator
def BFS_using_Queue(graph):
    frontier = Queue()
    frontier.put(start)
    came_from = dict()
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal: 
            break           

        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    current = goal # 목표 장소를 시작 장소로 지정
    path = [] # 역순으로 돌아오는 내용을 저장할 변수
    while current != start: # 현재 위치가 출발 위치일 때까지 수행
        path.append(current) # 현재 위치를 경로에 추가
        current = came_from[current] # 현재 위치 이동 전의 위치로 이동
    path.append(start) # 시작 위치를 포함시키기 위한 부분
    path.reverse() # 시작 ~ 도착으로 경로 순서를 변경

    print("BFS Queue Path = {}".format(path))

# BFS deque
@ time_check_decorator
def BFS_using_deque(graph):
    frontier = deque()
    frontier.append(start)
    came_from = dict()
    came_from[start] = None

    while frontier:
        current = frontier.popleft()

        if current == goal: 
            break           

        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.append(next)
                came_from[next] = current

    current = goal # 목표 장소를 시작 장소로 지정
    path = [] # 역순으로 돌아오는 내용을 저장할 변수
    while current != start: # 현재 위치가 출발 위치일 때까지 수행
        path.append(current) # 현재 위치를 경로에 추가
        current = came_from[current] # 현재 위치 이동 전의 위치로 이동
    path.append(start) # 시작 위치를 포함시키기 위한 부분
    path.reverse() # 시작 ~ 도착으로 경로 순서를 변경

    print("BFS deque Path = {}".format(path))

# Dijkstra PriorityQueue
@ time_check_decorator
def Dijkstra_using_PriorityQueue(graph):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        (_, current) = frontier.get()

        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put((priority, next))
                came_from[next] = current

    current = goal # 목표 장소를 시작 장소로 지정
    path = [] # 역순으로 돌아오는 내용을 저장할 변수
    while current != start: # 현재 위치가 출발 위치일 때까지 수행
        path.append(current) # 현재 위치를 경로에 추가
        current = came_from[current] # 현재 위치 이동 전의 위치로 이동
    path.append(start) # 시작 위치를 포함시키기 위한 부분
    path.reverse() # 시작 ~ 도착으로 경로 순서를 변경

    print("Dijkstra Path = {}".format(path))

# Dijkstra heapq
@ time_check_decorator
def Dijkstra_using_heapq(graph):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        (_, current) = heapq.heappop(frontier)

        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current

    current = goal # 목표 장소를 시작 장소로 지정
    path = [] # 역순으로 돌아오는 내용을 저장할 변수
    while current != start: # 현재 위치가 출발 위치일 때까지 수행
        path.append(current) # 현재 위치를 경로에 추가
        current = came_from[current] # 현재 위치 이동 전의 위치로 이동
    path.append(start) # 시작 위치를 포함시키기 위한 부분
    path.reverse() # 시작 ~ 도착으로 경로 순서를 변경

    print("Dijkstra Path = {}".format(path))

BFS_using_Queue(graph)
BFS_using_deque(graph)
Dijkstra_using_PriorityQueue(graph)
Dijkstra_using_heapq(graph)