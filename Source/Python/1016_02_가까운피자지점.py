# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:33:51 2022

@author: tjwjd
"""

# 2. 가까운 피자 지점

from collections import deque

def solution(V, road, branch):
    # 1부터 v까지
    pizza = [False] * (V+1)

    for b in branch:
        pizza[b] = b

    for i in range(1,V+1):
        # 지점이 있는 마을
        if pizza[i]:
            continue

        distance = [10001] * (V+1)
        # 해당 마을부터 시작
        q = deque()
        q.append(i)
        distance[i] = 0

        while True:
            if list(q) == []:
                break
            h = q.popleft()

            for r in road:
                if r[0] == h:
                    k = r[1]
                    dis_k = distance[h] + r[2]
                    if distance[k] > dis_k:
                        q.append(k)
                        distance[k] = dis_k
                elif r[1] == h:
                    k = r[0]
                    dis_k = distance[h] + r[2]
                    if distance[k] > dis_k:
                        q.append(k)
                        distance[k] = dis_k

        min_dis = 10000
        p = 0
        for b in branch:
            if distance[b] < min_dis:
                min_dis = distance[b]
                p = b

        pizza[i] = p


    answer = pizza[1:]
    return answer