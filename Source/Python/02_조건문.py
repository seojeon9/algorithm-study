# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:44:28 2022

@author: tjwjd
"""

# 조건문
x = 15

if x >= 10:
    print(x)
    
x = 90

if x >= 90 : 
    print("학점 : A")
elif x >= 80 :
    print("학점 : B")
elif x >= 70 :
    print("학점 : C")
else :
    print("학점 : F")
    
# 비교연산자
# x == y
# x != y
# x > y
# x < y
# x >= y
# x <= y

# 논리연산자
# x and y
# x or y
# not x

# 기타연산자
# x in 리스트
# x not in 리스트

score = 85

# pass
if score >= 80:
    pass # 나중에 작성할 소스코드
else :
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

# 부등식
x = 15
if 0 < x < 20:
    print('x는 0 이상 20 미만의 수입니다')
    


