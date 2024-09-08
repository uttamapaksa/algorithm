import sys; sys.setrecursionlimit(25000); input=sys.stdin.readline

N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dp = [[-1] * M for _ in range(N)]

def dfs(r, c):
    if r == N-1 and c == M-1:
        return 1
    if dp[r][c] == -1:
        dp[r][c] = 0
        for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if 0 <= nr < N and 0 <= nc < M and arr[r][c] > arr[nr][nc]:
                dp[r][c] += dfs(nr, nc)
    return dp[r][c]
dfs(0, 0)

print(dp[0][0])