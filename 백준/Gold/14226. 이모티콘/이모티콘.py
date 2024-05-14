from collections import deque

inf = 1 << 11
s = int(input())
dp = [[inf] * (s+1) for _ in range(s+1)]

q = deque([(1, 1)])
dp[1][1] = 1  # node, copy
while q:
    u, c = q.popleft()
    v = u - 1
    if 0 < v <= s:
        if dp[v][c] > dp[u][c] + 1:
            dp[v][c] = dp[u][c] + 1
            q.append((v, c))
    v = u + c
    if 0 < v <= s:
        if dp[v][c] > dp[u][c] + 1:
            dp[v][c] = dp[u][c] + 1
            q.append((v, c))
    if u != c:
        if dp[u][u] > dp[u][c] + 1:
            dp[u][u] = dp[u][c] + 1
            q.append((u, u))

print(min(dp[s]))