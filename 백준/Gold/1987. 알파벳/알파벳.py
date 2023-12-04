n, m = map(int, input().split())
arr = [[*(input())] for _ in range(n)]
visit = [[''] * m for _ in range(n)]

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
stack = [(0, 0, 1, arr[0][0])]
ans = 1

while stack:
    r, c, cnt, path = stack.pop()
    ans = max(ans, cnt)

    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= n or nc < 0 or nc >= m or arr[nr][nc] in path: continue
        new_path = path + arr[nr][nc]
        if visit[nr][nc] != new_path:
            visit[nr][nc] = new_path
            stack.append((nr, nc, cnt+1, new_path))

print(ans)