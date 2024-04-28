from collections import deque

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
M, N = map(int, input().split())
arr = [[*map(int, [*input()])] for _ in range(N)]
visit = [[10001] * M for _ in range(N)]

Q = deque()
Q.append((0, 0))
visit[0][0] = 0

while Q:
    r, c = Q.popleft()
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
        if arr[nr][nc] == 1:  # wall
            if visit[nr][nc] > visit[r][c] + 1:
                visit[nr][nc] = visit[r][c] + 1
                Q.append((nr, nc))
        else:  # no wall
            if visit[nr][nc] > visit[r][c]:
                visit[nr][nc] = visit[r][c]
                Q.append((nr, nc))

print(visit[N-1][M-1])