import sys
from collections import deque
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N = int(sys.stdin.readline())
graph = [[*map(int, input().split())] for _ in range(N)]
safezone = deque()
maxsafezonecnt = 1

minh, maxh = 101, -1
for i in range(N):
    for j in range(N):
        if graph[i][j] < minh:
            minh = graph[i][j]
        if graph[i][j] > maxh:
            maxh = graph[i][j]

for h in range(minh-1, maxh):
    safezonecnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > h and not(visited[i][j]):
                safezone.append((i, j))
                visited[i][j] = 1
                while safezone:
                    r, c = safezone.popleft()
                    for dr, dc in dir:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and h < graph[nr][nc] and not(visited[nr][nc]):
                            safezone.append((nr, nc))
                            visited[nr][nc] = 1
                safezonecnt += 1

    if safezonecnt > maxsafezonecnt:
        maxsafezonecnt = safezonecnt

print(maxsafezonecnt)