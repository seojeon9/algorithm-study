# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:16:13 2022

@author: tjwjd
"""

# 입출력
# input()
# 입력받은 데이터를 정수형 데이터로 처리하기 위해서는 
# 문자열을 정수로 바꾸는 int() 함수를 사용해야한다.

# 공백으로 구분되는 데이터를 받을 때
# list(map(int, input().split()))

# 입력을 위한 전형적인 소스코드
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

#%%
# 공백을 기준으로 구분하여 적은 수의 데이터 입력
# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)

#%%
# 입력을 빠르게 받아야 하는 경우
# 입력값이 많은 경우 input()을 사용하면 시간 초과를 받을 수 있다.
# 이때 파이썬의 sys 라이브러리에 있는 sys.sydin.readline() 함수를 이용한다.

import sys
# sys.stdin.readline().rstrip() 
# readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 공백 문자를 제거하기 위해
# rstrip() 함수를 사용해야 함

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)


#%%
# 변수를 문자열로 바꾸어 출력하는 소스코드 예시
# 출력할 변수들
answer = 7

print("정답은 " + str(answer) + "입니다.")
print(f"정답은 {answer}입니다.")

















