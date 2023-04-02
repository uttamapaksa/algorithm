from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N, M = map(int, input().split())
arr = [[*map(int, input())] for _ in range(N)]
visit = [[0] * M for _ in range(N)]
visit[0][0] = 1
q = deque([(0, 0, 1)])
while q:
    r, c, k = q.popleft()
    if r == N - 1 and c == M - 1:
        print(k)
        break
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M or visit[nr][nc] or not arr[nr][nc]: continue
        visit[nr][nc] = 1
        q.append((nr, nc, k + 1))
