# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 17:54:24 2022

@author: tjwjd
"""

# 구현
# 머릿속에 있는 알고리즘을 정확하고 빠르게 프로그램으로 작성하기
                                 
# int / long long           

# 1. 상하좌우
n = int(input())
guide = list(input().split(' '))     

x = [1,1]

for g in guide:
    if g == 'R':
        if x[1] == n:
            continue
        x[1] += 1
    elif g == 'L':
        if x[1] == 1:
            continue
        x[1] -= 1
    elif g == 'U':
        if x[0] == 1:
            continue
        x[0] -= 1
    else :
        if x[0] == n:
            continue
        x[0] += 1
        
print(x[0],x[1])

##############################################################################################################
#%%

# 2. 시각

# H를 입력 받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)

##############################################################################################################
#%%

# 3. 왕실의 나이트

x = input()
r = [2,2,-2,-2,1,-1,1,-1]
c = [1,-1,1,-1,2,2,-2,-2]

col = int(ord(x[0])) - int(ord('a')) + 1
row = int(x[1])


count = 0
for i in range(len(r)):
    if 1 <= col+c[i] <= 8  and 1 <= row+r[i] <= 8:
        count += 1
        
print(count)
    

##############################################################################################################
#%%

# 3. 게임 개발

map_size = list(map(int, input.split(' ')))
input_value = list(map(int, input.split(' ')))
x = [input_value[0], input_value[1]]
d = input_value[2]

world = []
for i in range(map_size[0]):
    world.append(list(map(int, input.split(' '))))
    
d_list = [0,3,2,1]
count = 0
while True:
    if d == 0:
        xx = x[0]-1
        yy = x[1]
        if xx >= 1 :
            if world[xx][yy] == 0:
                count += 1
                x[0] == xx
                world[xx][yy] = 2
            else:
                





direct = [0,3,2,1]















