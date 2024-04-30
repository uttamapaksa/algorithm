def dfs(u, k):
    global ans
    if k == 5:
        ans = 1
        return

    for v in G[u]:
        if V[v]: continue
        if ans: return
        V[v] = 1
        dfs(v, k+1)
        V[v] = 0


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

ans = 0
for u in range(N):
    V = [0] * N
    V[u] = 1
    dfs(u, 1)
print(ans)