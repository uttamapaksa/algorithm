from collections import deque


def sol(s):
    inf = 1 << 11
    dp = [[inf] * (s+1) for _ in range(s+1)]

    q = deque([(1, 1)])
    dp[1][1] = 1  # node, copy
    while q:
        u, uc = q.popleft()
        for v, vc in ((u-1, uc), (u+uc, uc), (u, u)):
            if v < 1 or v > s: continue
            if v == s:
                return dp[u][uc] + 1
            if dp[v][vc] > dp[u][uc] + 1:
                dp[v][vc] = dp[u][uc] + 1
                q.append((v, vc))


print(sol(int(input())))