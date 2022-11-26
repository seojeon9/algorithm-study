# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:54:01 2022

@author: tjwjd
"""

# 최댓값과 최솟값
def solution(s):
    a = list(map(int, s.split(' ')))
    min_a = min(a)
    max_a = max(a)
    answer = str(min_a) + ' ' + str(max_a)
    return answer


# JadenCase 문자열 만들기
def solution(s):
    s_list = s.split(' ')
    result = []
    for sl in s_list:
        sl = sl.capitalize()
        result.append(sl)
            
    answer = ' '.join(result)
    return answer


# 카펫
def solution(brown, yellow):
    n = int(brown / 2) - 2
    x = 0
    y = 0
    for i in range(1,n):
        if i * (n-i) == yellow:
            x = i
            y = n - i
    
    answer = [x+2,y+2]
    return answer

# 구명보트
def solution(people, limit):
    people.sort(reverse=True)
    result = 0
    count = 0
    
    g = [0] * len(people)
    index =  len(people)-1
    for i in range(len(people)):
        if g[i] == 0:
            result = people[i]
            for j in range(index,0,-1):
                if g[j] == 0:
                    result += people[j]
                    if result <= limit:
                        g[j] = 1
                        index = j
                    count += 1
                    break
        
         
    answer = count
    return answer