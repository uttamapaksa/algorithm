dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

n, m = map(int, input().split())
arr = [list(map(ord, input())) for _ in range(n)]
visit = {arr[0][0]}
ans = 1

def dfs(r, c, k):
    global ans
    ans = max(ans , k)

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            char = arr[nr][nc]
            if char not in visit:
                visit.add(char)
                dfs(nr, nc, k+1)
                visit.discard(char)
dfs(0, 0, 1)

print(ans)