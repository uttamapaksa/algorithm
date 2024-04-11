def dfs(p, d):
    stack = [(p, d)]
    depth[p] = d
    par[0][p] = p
    while stack:
        p, d = stack.pop()
        for c in G[p]:
            if par[0][c]: continue
            depth[c] = d + 1
            par[0][c] = p
            stack.append((c, d + 1))

def parentDP():
    for j in range(1, LOG):
        for i in range(1, N+1):
            par[j][i] = par[j-1][par[j-1][i]]

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a  # depth[a] > depth[b]
    for i in range(LOG-1, -1, -1):
        if (depth[a] - depth[b]) >= (1 << i):
            a = par[i][a]
    if a == b:
        return a
    for i in range(LOG-1, -1, -1):
        if par[i][a] != par[i][b]:
            a = par[i][a]
            b = par[i][b]
    return par[0][a]


N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

LOG = 17  # 2 ** 16 > N
par = [[0] * (N+1) for _ in range(LOG)]
depth = [0] * (N+1)

dfs(1, 0)
parentDP()

answer = ""
M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    answer += f'{lca(u, v)}\n'

print(answer)