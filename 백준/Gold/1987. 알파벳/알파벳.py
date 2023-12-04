delta = ((-1, 0), (0, -1), (1, 0), (0, 1))

n, m = map(int, input().split())
arr = [[*(input())] for _ in range(n)]
ans = 1

stack = [(0, 0, 1, arr[0][0])]
while stack:
    r, c, cnt, visit = stack.pop()
    ans = max(ans, cnt)

    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= n or nc < 0 or nc >= m or arr[nr][nc] in visit: continue
        stack.append((nr, nc, cnt+1, visit + arr[nr][nc]))

print(ans)