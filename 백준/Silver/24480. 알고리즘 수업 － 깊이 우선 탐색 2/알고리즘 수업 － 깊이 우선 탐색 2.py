import sys; sys.setrecursionlimit(10**5); input=sys.stdin.readline

def dfs(u):
    global order; order += 1
    visit[u] = order
    for v in G[u]:
        if visit[v]: continue
        dfs(v)

N, M, R = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
for u in G:
    u.sort(reverse=True)

order = 0
visit = [0] * (N+1)
dfs(R)
print(*visit[1:], sep='\n')