# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:40:46 2022

@author: tjwjd
"""

# 이진 탐색
# 탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘

# 재귀 함수로 구현한 이진 탐색 소스 코드
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)
    
# n과 target을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
    
    
    
##############################################################################################################
#%%


# 2. 부품 찾기
n = int(input())
a = list(map(int, input().split(' ')))
m = int(input())
b = list(map(int, input().split(' ')))

a.sort()

def b_search(array, target, start, end ):
    # 시작점과 끝점으로 중간점을 구한다
    mid = (start + end ) // 2
    if mid < start:
        return None
    if a[mid] == target:
        return True
    # 중간점과 타켓을 비교하여 중간점이 더 크면 왼쪽으로
    elif a[mid] > target:
        b_search(array, target, start, mid-1)
    else:
        b_search(array, target, mid+1, end)


for i in b:
    if b_search(a, i, 0, n) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
        
##############################################################################################################
#%%

# 3. 떡볶이 떡 만들기

n, m = map(int, input().split(' '))
a = list(map(int, input().split(' ')))

a.sort()

start = 0
end = a[n-1]

mid = 0
while True:
    mid = (start + end) // 2
    result = 0
    for i in a:
        if i > mid:
            result += i - mid
    if m == result:
        break
    elif result > m:
        start = mid + 1
    else:
        end = mid -1

print(mid)



































