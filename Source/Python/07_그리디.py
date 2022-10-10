# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:36:44 2022

@author: tjwjd
"""

# 그리디
# 현재 상황에서 가장 좋아 보이는 것만을 선택하는 알고리즘

# 1. 당장 좋은 것만 선택하는 그리디

# 3-1 거스름돈
n = 1260
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin
    
print(count)

##############################################################################################################
#%%
# 2. 큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징

n, m, k = map(int,input().split(' '))
data = list(map(int,input().split(' ')))
sum = 0

data.sort(reverse = True)
first = data[0]
sec = data[1]

while True:
    for i in range(k):
        if m == 0:
            break
        sum += first
        m -= 1
    if m == 0:
        break
    sum += sec
    m -= 1
    
print(sum)

# => 하지만 이렇게 문제를 해결했을 때 M의 크기가 100억 이상으로 커진다면 시간초과 판정을 받는다.
#%%
# 2-2 새로운 아이디어

n, m, k = map(int,input().split(' '))
data = list(map(int,input().split(' ')))
sum = 0

data.sort(reverse = True)
first = data[0]
sec = data[1]

it = first * k + sec

sum = it*(m//(k+1)) + first * (m%(k+1))

print(sum)

##############################################################################################################
#%%

# 3. 숫자 카드 게임

n, m = map(int, input().split(' '))

min_list = []
for i in range(n):
    data = list(map(int, input().split(' ')))
    min_list.append(min(data))

result = max(min_list)

print(result)

##############################################################################################################
#%%

# 4. 1이 될 때까지

n, k = map(int, input().split(' '))
count = 0

while True:
    if n % k == 0:
        n /= k
    else :
        n -= 1
    count += 1
    if n == 1:
        break

print(count)
















