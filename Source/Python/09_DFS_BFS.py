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


# 탐색 알고리즘 DFS/ BFS








































