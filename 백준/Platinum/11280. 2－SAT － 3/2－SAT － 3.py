import sys; sys.setrecursionlimit(10**4)

N, M = map(int, input().split())
L = 2*(N+1)
G = [set() for _ in range(L)]
for _ in range(M):
    a, b = map(int, input().split())
    G[-a].add(b)
    G[-b].add(a)

# SCC
def tarjan(u):
    global id, ans
    id += 1
    ids[u] = par = id
    stack.append(u)
    for v in G[u]:
        if not ids[v]:
            par = min(par, tarjan(v))
        elif not finished[v]:
            par = min(par, ids[v])
    if par == ids[u]:
        curr = set()
        while 1:
            v = stack.pop()
            finished[v] = True
            if -v in curr:
                ans = 0
            curr.add(v)
            if u == v:
                break
    return par

id = 0
ids = [0] * L
finished = [False] * L
stack = []
ans = 1
for u in range(L):
    if not ids[u]:
        tarjan(u)

print(ans)