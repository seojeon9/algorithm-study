| 상황        | 선택      |
| --------- | ------- |
| 중복/빠른조회   | 해시      |
| 연결/그래프    | DFS/BFS |
| 최단거리      | BFS     |
| 모든 경우     | DFS     |
| 최소/최대 선택  | 그리디     |
| 기준 정해서 뽑기 | 정렬      |

# 1. 해시
## 문제 유형 및 키워드
- 중복 체크, 빠른 조회, 빈도수 계산, 매핑/그룹핑
- 한번에 찾기, 이미 본 값인지, 개수 세기

## 대표 문제 유형
- TWO SUM
- 문자열 빈도수
- 중복 제거
- 가장 많이 나온 값

## 풀이 방법
1. set -> 존재 여부
```
nums = [1,2,3,4,]
s = set()

for n in nums:
    if n in s:
        print("중복")
    s.add(n)
```

2. dict -> 카운팅
```
from collections import defaultdict

cnt = defaultdict(int)

for n in nums:
    cnt[n] += 1
```

3. 핵심 패턴(TWO SUM)
```
nums = [2,7,11,15]
target = 9
d = {}

for i, n in enumerate(nums):
    if target - n in d:
        print(d[target-n], i)
    d[n] = i
```
-> "지금 값 기준으로 필요한 값이 이미 있는지 확인"

# DFS/BFS
## 문제 유형 및 키워드
- 그래프 탐색, 연결될 것 찾기, 최단 거리(BFS), 모든 경우 탐색(DFS)
- 몇 개의 그룹, 연결된 영역, 최단 거리

## 대표 문제 유형
- 섬 개수
- 미로 탐색
- 네크워트 개수
- 최단 거리

## 풀이 방법
1. BFS(최단거리용)
```
from collections import deque

def bfs(start):
    q = deque([start])
    visited = set([start])

    while q:
        cur = q.popleft()
        for next not in graph[cur]:
            if next not in visited:
                visited.add(next)
                q.append(next)
```
-> 먼저 들어간 게 먼저 나옴(Queue) / 거리,최단 경로

2. DFS(탐색/조합용)
```
def dfs(node):
    visited.add(node)

    for next in graph[node]
        if next not in visited:
            dfs(next)
```
-> 깊게 들어감 / 모든 경우 탐색

#. 2차원(진짜 자주 나옴)
```
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
```
-> 방문 처리 + 범위 체크

# 정렬 + 그리디
## 문제 유형
- 최소/최대 선택, 조건 만족하면서 최적 선택, 정렬 후 규칙 적용
- 가장 작은/큰, 최대로 만들기, 최소 비용

## 대표 문제 유형
- 회의실 배정
- 거스름돈
- 가장 큰 수 만들기
- 작업 스케줄링

## 풀이 방법
1. 정렬 후 순차 선택
```
arr.sort()

for x in arr:
    #  조건 만족하면 선택
```

2. 기준 바꿔서 정렬
```
arr.sort(key=lambda x: x[1]) # 두번째 값 기준
```

3. 회의실 배정(핵심 예제)
```
meeting.sort(key=lamnda x: (x[1], x[0]))

end = 0
count = 0

for s, e int meetings:
    if s >= end:
        count += 1
        end = e
```
-> 빨리 끝나는 것부터 선택

4. 거스름돈(그리디 기본)
```
coins = [500,100,50,10]
n = 1260
count = 0

for coin in coins:
    count += n // coin
    n %= coin
```


해시 → “빠르게 찾기”
BFS → “최단 거리”
DFS → “다 탐색”
그리디 → “지금 최선 선택”

---
# 프로그래머스 실전 문제
## 해시
1. 폰켓몬 (Lv1)
https://school.programmers.co.kr/learn/courses/30/lessons/1845

2. 완주하지 못한 선수 (Lv1)
https://school.programmers.co.kr/learn/courses/30/lessons/42576

3. 전화번호 목록 (Lv2)
https://school.programmers.co.kr/learn/courses/30/lessons/42577

4. 의상 (Lv2)
https://school.programmers.co.kr/learn/courses/30/lessons/42578

5. 베스트앨범 (Lv3)
https://school.programmers.co.kr/learn/courses/30/lessons/42579

## DFS/BFS
6. 타겟 넘버 (Lv2)
https://school.programmers.co.kr/learn/courses/30/lessons/43165

7. 네트워크 (Lv3)
https://school.programmers.co.kr/learn/courses/30/lessons/43162

8. 단어 변환 (Lv3)
https://school.programmers.co.kr/learn/courses/30/lessons/43163

9. 여행경로 (Lv3)
https://school.programmers.co.kr/learn/courses/30/lessons/43164

10. 게임 맵 최단거리 (Lv2)
https://school.programmers.co.kr/learn/courses/30/lessons/1844

## 정렬 + 그리디
11. 체육복 (Lv1)
https://school.programmers.co.kr/learn/courses/30/lessons/42862

12. 큰 수 만들기 (Lv2)
https://school.programmers.co.kr/learn/courses/30/lessons/42883

13. 구명보트 (Lv2)
https://school.programmers.co.kr/learn/courses/30/lessons/42885

14. 섬 연결하기 (Lv3)
https://school.programmers.co.kr/learn/courses/30/lessons/42861

15. 단속카메라 (Lv3)
https://school.programmers.co.kr/learn/courses/30/lessons/42884