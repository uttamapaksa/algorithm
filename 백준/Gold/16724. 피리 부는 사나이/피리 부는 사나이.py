def dfs(r, c):
    stack = [[r, c]]
    while stack:
        r, c = stack.pop()
        for dir in range(4):
            dr, dc = delta[dir]
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visit[nr][nc]: continue
            if arr[nr][nc] == dir:
                visit[nr][nc] = 1
                stack.append((nr, nc))
            elif arr[r][c] == (dir + 2) % 4:
                visit[nr][nc] = 1
                stack.append((nr, nc))

delta = ((0, -1), (-1, 0), (0, 1), (1, 0))
dirs = {"R": 0, "D": 1, "L": 2, "U": 3}
N, M = map(int, input().split())
arr = [[dirs[char] for char in input()] for _ in range(N)]
visit = [[0] * M for _ in range(N)]

ans = 0
for r in range(N):
    for c in range(M):
        if visit[r][c]: continue
        ans += 1
        visit[r][c] = 1
        dfs(r, c)

print(ans)