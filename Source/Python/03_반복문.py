# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 18:38:34 2022

@author: tjwjd
"""

# 반복문
# while문
i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1
    
print(result)

i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    if i % 2== 1:
        result += i
    i += 1
    
print(result)

# for문
result = 0

# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10):
    result += i
    
print(result)

# range()의 값으로 하나의 값만을 넣으면 자동으로 시작 값은 0이 된다.

scores = [90,85,77,65,97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")
        

# continue
scores = [90,85,77,65,97]
black_list = {2,4}


for i in range(5):
    if i + 1 in black_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

for i in range(2,10) :
    for j in range(1,10) :
        print(i, "X", j ,"=", i * j)
    print()
        
        
        
        
        
        
        
        
        
        
        
        
        