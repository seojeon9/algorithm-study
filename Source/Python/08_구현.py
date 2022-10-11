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

# n, m을 공백으로 구문하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x좌표, y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# [0,3,2,1]
# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else :
        turn_time +=1
    # 네 방향 모두 갈 수 없는 경우
    if turn_timr += 1:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time=0
  
# 정답출력
print(count)






































