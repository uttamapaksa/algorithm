from collections import deque

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

N = int(input())
arr = [input().split() for _ in range(N)]
S, T = [], []  # 학생좌표, 선생좌표

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S':
            S.append((i, j))  # 학생좌표 저장
        elif arr[i][j] == 'T':
            T.append((i, j))  # 선생좌표 저장


cannot = 0  # 회피 불가능 여부
obs = set()  # 장애물 가능범위('S'와 인접한 'X') 세트
Q = deque(S)
while Q:
    if cannot: break
    r, c = Q.popleft()
    for i in range(4):  # 각 학생 동서남북 검사
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] == 'S': continue
        if arr[nr][nc] == 'T': cannot = 1; break  # 선생님이 붙어있는 경우: 회피 불가능 
        if arr[nr][nc] == 'X': obs.add((nr, nc))
L = len(obs)


def canEvade():  # 회피 가능 여부 체크 함수
    Q = deque(T)  # 선생님 좌표
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r, c
            while 1:  # 동서남북 끝까지 탐색
                nr, nc = nr + dr[i], nc + dc[i]
                if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] == 'T': break  # 선생님(장애물) 발견
                if arr[nr][nc] == 'S': return 0  # 학생 발견
    return 1


# 출력부
if cannot:  # 선생님이 붙어있는 경우: 불가능
    print('NO')
elif L <= 3:  # 노출된 부분이 3개 이하인 경우: 가능
    print('YES')
else:
    obs = list(obs)  # 장애물 가능범위 리스트
    used = [0] * L
    can = 0  # 회피 가능 여부
    
    def comb(k):  # 장애물 모든 조합 순회
        global can
        if can: #  회피 가능하면 무한 return
            return
        if k == 3:
            if canEvade(): # 한번이라도 피할 수 있다면
                can = 1
            return
        
        for i in range(L):
            if used[i]: continue
            used[i] = 1
            r, c = obs[i]
            arr[r][c] = 'T'  # 선생님(T)을 만나도 탐색 멈추기로 되어있기 때문에 장애물을 그냥 'T'로 설정
            comb(k+1)
            arr[r][c] = 'X'  # 백트래킹
            used[i] = 0
    comb(0)
    
    if can: print('YES')
    else: print('NO')