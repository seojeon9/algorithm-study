# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:56:02 2022

@author: tjwjd
"""

# 최단경로 실전문제

# 미래도시 -> 플로이드 워셜


INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
for k in range(1, n+1):
    for a in range(a, n+1):
        for b in range(a, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)