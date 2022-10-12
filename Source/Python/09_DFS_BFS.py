# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:57:15 2022

@author: tjwjd
"""

# 꼭 필요한 자료구조 기초
# 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
# 자료구조 : 데이터를 표현하고 관리하고 처리하기 위한 구조
# 삽입 : 데이터를 삽입한다 / 삭제 : 데이터를 삭제한다

# stack
stack = []

stack.append(5)
stack.append(2)
print(stack.pop())
print(stack.pop())

# queue

from collections import deque

queue = deque()

queue.append(5)
queue.append(3)
print(queue.popleft())
print(queue.popleft())

# 재귀함수 : 자기 자신을 다시 호출하는 함수

def recursive_fun():
    print('재귀 함수를 호출합니다.')
    recursive_fun()
# RecursionError: maximum recursion depth exceeded while calling a Python object
# recursive_fun()


def recursive_fun1(i):
    # 100번째 출력하였을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 함수에서 ' , i+1 ,'번째 재귀 함수를 호출합니다.')
    recursive_fun1(i+1)
    print(i, '번째 함수를 종료합니다.')

recursive_fun1(1)

##############################################################################################################
#%%
# 탐색 알고리즘 DFS/ BFS
# DFS : 깊이 우선 탐색 - 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

# 인접행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식

INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 인접리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식
# 행이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))

print(graph)

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4,],
    [7,8],
    [2,6,8],
    [1,7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

##############################################################################################################
#%%

# BFS : 너비 우선 탐색 - 가가운 노드부터 탐색하는 알고리즘
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4,],
    [7,8],
    [2,6,8],
    [1,7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)


#           DFS             BFS
# 동작원리  스택              큐
# 구현방법  재귀 함수 이용    큐 자료구조 이용

##############################################################################################################
#%%

# 3. 음료수 얼려 먹기

n, m = map(int, input().split())

g = []
for i in range(n):
    g[i].append(list(map(int, input())))
    
# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if g[x][y] == 0:
        # 해당 노드 방문 처리
        g[x][y] = 1
        # 상하좌우 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력

##############################################################################################################
#%%

# 4. 미로 탈출

from collections import deque

n, m = map(int, input().split())

g = []
for i in range(n):
    g.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    q = deque()
    q.append((x,y))
    # 큐가 빌 때 까지 계속
    while q:
        x, y = q.popleft()
        # 현재 위치에서 네 방형으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            # 벽인 경우 무시
            if g[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if g[nx][ny] == 1:
                g[nx][ny] = g[x][y] + 1
                q.append((nx,ny))
        # 가장 오른쪽 아래까지의 최단 거리 반환
        return g[n-1][m-1]
    
# BFS를 출력한 결과 출력
print(bfs(0,0))
            


























