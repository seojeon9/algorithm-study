# 정수형

a = 2000 # 양의 정수
print(a)

a = -7 # 음의 정수
print(a)

a = 0
print(0)

# 실수형
# 양의 실수
a = 157.93
print(a)

# 음의 실수 
a = -1337.2
print(a)

# 소수부가 0일 때 0을 생략
a = 5.
print(a)

# 정수부가 0일 때 0을 생략
a = -.7
print(a)

# 10억의 지수 표현 방식
a = 1e9
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 394e-3
print(a)

a = 0.3 + 0.6
print(a) # 0.89999999

if a == 0.9:
    print(True)
else :
    print(False)
    
# False
# 컴퓨터는 실수를 정확히 표현 못 한다.

a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else :
    print(False)
    
##########################################
#%%

# 수 자료형의 연산
a = 7
b = 3

# 나누기
print(a / b)

# 나머지
print(a % b)

# 몫
print(a // b)

# 거듭제곱
a = 5
b = 3

print(a ** b)

############################################
#%%

# 리스트 자료형
a = [1,2,3,4,5,6,7,8,9]
print(a)

# 인덱스 4, 즉 다섯 번째 원소에 접근
print(a[4])

# 빈 리스트 선언 방법 1)
a = list()
print(a)

# 빈 리스트 선언 방법 2)
a = []
print(a)

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)


# 리스트의 인덱싱과 슬라이싱
a = [1,2,3,4,5,6,7,8,9]
# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 네번째 원소 값 변경
a[3] = 7
print(a)

# 슬라이싱
a = [1,2,3,4,5,6,7,8,9]

# 두번째 원소부터 네 번째 원소까지
print(a[1:4])

# 리스트 컴프리헨션
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
a = [i*i for i in range(10)]
print(a)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# 언더바(_)는 어떤 역할?
# 파이썬 자료구조/ 알고리즘에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바를 자주 사용한다.

a = [1,4,3]
print("기본 리스트: ", a)

# 리스트에 원소 삽입
a.append(2)
print(a)

# 오름차순 정렬
a.sort()
print(a)

# 내림차순 정렬
a.sort(reverse = True)
print(a)

# 리스트의 원소 뒤집기
a.reverse()
print(a)

# 특정 인덱스에 데이터 추가
a.insert(2,3)
print(a)

# 특정 값인 데이터 개수 세기
print(a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print(a)



















