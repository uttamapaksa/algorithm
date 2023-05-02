import sys; input = sys.stdin.readline
from collections import deque
from copy import deepcopy

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    q = deque(deepcopy(twoarr))
    v = deepcopy(visit)
    tmpZ = Z-3
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nc < 0 or nr == N or nc == M or v[nr][nc]: continue
            q.append((nr, nc))
            v[nr][nc] = 1
            tmpZ -= 1

    global ans
    ans = max(ans, tmpZ)


N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
zeroarr = []
twoarr = []
visit = [[0] * M for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            zeroarr.append((i, j))
        elif arr[i][j] == 2:
            twoarr.append((i, j))
            visit[i][j] = 1
        else:
            visit[i][j] = 1

Z = len(zeroarr)
for j in range(Z-2):
    r1, c1 = zeroarr[j]
    visit[r1][c1] = 1
    for k in range(j+1, Z-1):
        r2, c2 = zeroarr[k]
        visit[r2][c2] = 1
        for l in range(k+1, Z):
            r3, c3 = zeroarr[l]
            visit[r3][c3] = 1
            bfs()
            visit[r3][c3] = 0
        visit[r2][c2] = 0
    visit[r1][c1] = 0

print(ans)