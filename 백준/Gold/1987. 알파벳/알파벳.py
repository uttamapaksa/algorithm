dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

n, m = map(int, input().split())
arr = [list(map(ord, input())) for _ in range(n)]
ans = 1

stack = [(0, 0, 1, {arr[0][0]})]
while stack:
    r, c, cnt, visit = stack.pop()
    ans = max(ans, cnt)

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= m or arr[nr][nc] in visit: continue
        new_visit = visit.copy()
        new_visit.add(arr[nr][nc])
        stack.append((nr, nc, cnt+1, new_visit))

print(ans)