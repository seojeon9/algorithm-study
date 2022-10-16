# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:33:05 2022

@author: tjwjd
"""

# 1. 가위바위보

def solution(rsp3):
    # 누적 점수
    # a,b,c
    score = [0] * 3
    w = ['R','S','P']
    l = ['S','P','R']
    # 누가 이겼는지 판단
    for v in rsp3:
        a = v[0]
        b = v[1]
        c = v[2]
        if a == b and b == c:
            continue
        if a != b and b != c and c != a:
            continue

        if a == b:   
            t = a 
            k = c
            num1 = 0
            num2 = 1
            num3 = 2
        elif b == c:
            t = b
            k = a
            num1 = 1
            num2 = 2
            num3 = 0
        elif c == a:
            t = c
            k = b
            num1 = 2
            num2 = 0
            num3 = 1

        for i in range(len(w)):
            if t == w[i]:
                if k == l[i]:
                    if score[num1] == score[num2]:
                        score[num1] += 1
                        score[num2] += 1
                    elif score[num1] > score[num2]:
                        score[num2] += 2
                    else :
                        score[num1] += 2
                else : 
                    score[num3] += 2

    answer = score
    return answer