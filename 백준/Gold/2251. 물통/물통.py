def dfs(a, b, c):
    if visit[a][b][c]:
        return
    visit[a][b][c] = 1
    if not a:
        ans.add(c)
    ra, rb, rc = A-a, B-b, C-c
    dfs(a - min(a, rb), b + min(a, rb), c)
    dfs(a - min(a, rc), b, c + min(a, rc))
    dfs(a + min(b, ra), b - min(b, ra), c)
    dfs(a, b - min(b, rc), c + min(b, rc))
    dfs(a + min(c, ra), b, c - min(c, ra))
    dfs(a, b + min(c, rb), c - min(c, rb))


A, B, C = map(int, input().split())
visit = [[[0] * (C+1) for _ in range(B+1)] for _ in range(A+1)]
ans = set()
dfs(0, 0, C)

print(*sorted(ans))