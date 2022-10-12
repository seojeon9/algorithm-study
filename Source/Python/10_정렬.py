# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:36:24 2022

@author: tjwjd
"""

# 정렬
# 연속된 데이터를 기준에 따라서 정렬하기 위한 알고리즘

# 선택 정렬

array = [3,2,1,6,5,4,7,6,5,8,7,9,0]
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)

# 삽입 정렬
array = [3,2,1,6,5,4,7,6,5,8,7,9,0]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j] , array[j -1] = array[j -1], array[j]
        else :
            break

print(array)


# 퀵 정렬

# 계수 정렬

# 정렬 라이브러리
array = [3,2,1,6,5,4,7,6,5,8,7,9,0]
result = sorted(array)
print(result)


array = [3,2,1,6,5,4,7,6,5,8,7,9,0]
array.sort()
print(array)

# sort() 함수에 key 매개변수 입력

array = [('바나나',2),('사과', 5),('당근',3)]

def setting(data):
    return data[1]

array.sort(key=setting)
print(array)


##############################################################################################################
#%%

# 2. 위에서 아래로

n = int(input())

a = []
for i in range(n):
    a.append(int(input()))
    
a.sort(reverse=True)

for i in a:
    print(i, end=' ')
    
    
##############################################################################################################
#%%

# 3. 성적이 낮은 순서로 학생 출력하기   

n = int(input())

a = []
for i in range(n):
    input_data = list(input().split(' '))
    a.append((input_data[0], int(input_data[1])))
   
a.sort(key=lamda a: a[1])
print(a)

##############################################################################################################
#%%

# 4. 두 배열의 원소 교체

n, k = map(int, input().split(' '))

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] , b[i] = b[i], a[i]
        
print(sum(a))


















