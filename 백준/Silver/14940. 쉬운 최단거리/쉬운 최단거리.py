from collections import deque

# delta
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

# input part
n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
ans = [[0] * m for _ in range(n)]

# find 'start point'
stop = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2: 
            stop = 1
            break
    if stop: break

# BFS. set 'reachable point'
Q = deque()
Q.append((i, j))

while Q:
    r, c = Q.popleft()
    val = ans[r][c]
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if nr < 0 or nr >= n or nc < 0 or nc >= m or ans[nr][nc] or not arr[nr][nc]:
            continue
        ans[nr][nc] = val + 1
        Q.append((nr, nc))

# set 'unreachable point' to '-1'
for r in range(n):
    for c in range(m):
        if arr[r][c] and not ans[r][c]:
            ans[r][c] = -1

# set 'start point' to '0'
ans[i][j] = 0

# output part
for line in ans:
    print(*line)