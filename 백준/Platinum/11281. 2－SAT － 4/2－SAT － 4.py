import sys; sys.setrecursionlimit(10**5); input=sys.stdin.readline

# input
N, M = map(int, input().split())
L = 2*N+1
G = [[] for _ in range(L)]
for _ in range(M):
    a, b = map(int, input().split())
    G[-a].append(b)
    G[-b].append(a)

# SCC
def tarjan(u):
    global id, scc_id
    id += 1
    ids[u] = par = id
    stack.append(u)
    for v in G[u]:
        if not ids[v]:
            par = min(par, tarjan(v))
        elif not scc_ids[v]:
            par = min(par, ids[v])
    if par == ids[u]:
        scc_id += 1
        while 1:
            v = stack.pop()
            if scc_ids[-v] == scc_id:
                print(0)
                exit()
            scc_ids[v] = scc_id
            if v == u:
                break
    return par

id = 0
ids = [0] * L
scc_id = 0
scc_ids = [0] * L
stack = []
for u in range(1, N+1):
    if not ids[u]:
        tarjan(u)
for u in range(-N, 0):
    if not ids[u]:
        tarjan(u)

# output
ans = [1] * (N+1)
for u in range(1, N+1):
    if scc_ids[u] > scc_ids[-u]:
        ans[u] = 0
print(1)
print(*ans[1:])