# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 02:23:16 2022

@author: tjwjd
"""

# 주요 라이브러리의 문법과 유의점

# 표준 라이브러리 : 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리를 의미한다.

# 내장 함수 : print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 하이브러리이다.
# 파이썬 프로그램을 작성할 때 없어서는 안되는 필수적인 기능을 포함하고 있다.

# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리이다. 
# 순열과 조합 라이브러리를 제공한다.

# heapq : 힙(heap) 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용한다.

# bisect : 이진 탐색(Binary Search) 기능을 제공하는 라이브러리이다.

# collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리이다.

# math : 필수적인 수학적 기능을 제공하는 라이브러리이다. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 부터
# 파이(pi)와 같은 상수를 포함하고 있다.

##############################################################################################################
# 내장 함수
result = sum([1,2,3,4,5])
print(result)

print(min(7,3,5,2))

print(max(7,3,5,2))

# eval() : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환
result = eval("(3+5)*7")
print(result)

# sorted()
print(sorted([9,3,5,7,8]))
print(sorted([9,3,5,7,8], reverse = True))

# 리스트의 원소로 리스트나 튜플이 존재할 때 특정한 기준에 따라서 정렬을 수행 할 수 있음
result = sorted([('홍길동',35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result)

# 리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하고 있음
data = [9,7,8,4,2,6]
data.sort()
print(data)

##############################################################################################################
#%%
# itertools
# : 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.

# permutations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는
#               모든 경우(순열)를 계산해준다.

from itertools import permutations

data = ['A', 'B', 'C'] 
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)


# combiactions : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고
#               나열하는 모든 경우(조합)를 계산한다.

from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기

print(result)


# product : permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로
#           나열하는 모든 경우(순열)를 계산한다. 다만 원소를 중복하여 뽑는다.
#           product 객체를 초기화 할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다.

from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기((중복 허용))
print(result)


# combinations_with_replacement : combinations와 같이 리스트와 같은 itertable 객체에서 
#                               r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다.
#                               다만 원소는 중복해서 뽑는다.

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)

##############################################################################################################
#%%

# heapq
# heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용
# 최소 힙으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.

import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 최대힙 만들기 : 원소의 부호를 임시로 변경하는 방식
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

##############################################################################################################
#%%

# bisect
# 이진 탐색을 쉽게 구현할 수 있는 라이브러리
# 정렬된 배열에서 특정한 원소를 찾아야 할 때 매우 효과적

# bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# count_by_range(a, left_value, right_value)
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, lvalue, rvalue):
    rindex = bisect_right(a, rvalue)
    lindex = bisect_left(a, lvalue)
    return rindex - lindex

a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4)) 

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))

##############################################################################################################
#%%

# collections
# deque, Counter

# deque
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

# Counter
from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

##############################################################################################################
#%%

# math

import math

# 팩토리얼
print(math.factorial(5))

# 제곱근
print(math.sqrt(7))

# 최대 공약수
print(math.gcd(21, 14))

# 파이
print(math.pi)
# 자연상수 e
print(math.e)




