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

# 특정 값 데이터 모두 삭제
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)

############################################
#%%

# 문자열 자료형
data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 문자열 연산
a = 'hello'
b = 'world'

print(a + " " + b)

a = 'string'
print(a * 3)

a = "ABCDEF"
print(a[2:4])

# 튜플 자료형
# 튜플을 한번 선언된 값을 변경할 수 없다.
# 리스트는 대괄호를 이용하지만, 튜플은 소괄호를 이용한다.

a = (1,2,3,4)
print(a)

# a[2] = 7 # TypeError: 'tuple' object does not support item assignment


# 튜플 자료형 -> 그래프 알고리즘을 구현할 때 자주 사용
# 다익스트라 최단 경로 알고리즘처럼 최단 경로르 찾아주는 알고리즘의 내부에서는 우선순위 큐를 이용하는데 
# 해당 알고리즘에서 우선순위 큐에 한 번 들어간 값은 변하지 않는다.
# 그래서 그 우선순위 큐에 들어가는 데이터를 튜플로 구성하여 소스코드를 작성한다.
# 이렇게 알고리즘을 구현하는 과정에서 일부로 튜플을 이용하게 되면 
# 혹여나 자신이 알고리즘을 잘못 작성함으로써 변경하면 안 되는 값이 변경되고 있지는 않은지 체크할 수 이ㅣㅆ다.
# 또한 튜플은 리스트에 비해 상대적으로 공간 효율적이고, 일반적으로 각 원소의 성질이 다를 때 주로 사용한다.
# 다익스트라 최단 경로 알고리즘에서는 '비용'과 '노드 번호' 라는 다른 성질의 데이터를 
# (비용, 노드 번호)의 형태로 함께 튜플로 묶어서 관리하는 것이 관례이다


############################################
#%%

# 사전 자료형
# - 키 쌍으로 구성되는 데이터

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재 합니다.", data['사과'])
    
# iterable 자료형 : 리스트, 문자열, 튜플 -> in 문법 사용 가능

# 사전 자료형 관련 함수
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])
    
############################################
#%%

# 집합 자료형
# 중복을 허용하지 않는다.
# 순서가 없다.

# 집합 자료형 초기화 방법 1
data = set([1,1,3,4,5,5,6])
print(data)

# 집합 자료형 초기화 방법 2
data = {1,1,2,3,4,4,5}
print(data)

# 집합 자료형의 연산
a = {1,2,3,4,5}
b = {3,4,5,6,7}

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

# 집합 자료형 관련 함수
data = {1,2,3}
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5,6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)



















