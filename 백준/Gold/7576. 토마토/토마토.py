import sys; input=sys.stdin.readline

from collections import deque

M, N = map(int, input().split())
tomato = [[*map(int, input().split())] for _ in range(N)]
zero = 0
queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))
        elif tomato[i][j] == 0:
            zero += 1

if zero == 0:
    print(0)
else:
    while queue:
        r, c = queue.popleft()
        for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if nr < 0 or nr >= N or nc < 0 or nc >= M or tomato[nr][nc]: continue
            tomato[nr][nc] = tomato[r][c] + 1
            queue.append((nr, nc))
            zero -= 1
    if zero:
        print(-1)
    else:
        print(tomato[r][c] - 1)