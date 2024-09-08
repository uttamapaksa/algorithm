import sys; sys.setrecursionlimit(5000); input=sys.stdin.readline

# input
flag = {'R': -1, 'B': 1}
k, n = map(int, input().split())
L = 2*(k+1)
G = [set() for _ in range(L)]
for _ in range(n):
    a, af, b, bf, c, cf = input().split()
    a, b, c = int(a) * flag[af], int(b) * flag[bf], int(c) * flag[cf]
    G[-a].add(b); G[-a].add(c)
    G[-b].add(c); G[-b].add(a)
    G[-c].add(a); G[-c].add(b)

# SCC
def tarjan(u):
    global id
    id += 1
    ids[u] = par = id
    stack.append(u)
    for v in G[u]:
        if not ids[v]:
            par = min(par, tarjan(v))
            if not par:
                return 0
        elif not scc_ids[v]:
            par = min(par, ids[v])
    if par == ids[u]:
        global scc_id
        scc_id += 1
        while 1:
            v = stack.pop()
            if scc_ids[-v] == scc_id:
                return 0
            scc_ids[v] = scc_id
            if u == v:
                break
    return par

id = 0
ids = [0] * L
scc_id = 0
scc_ids = [0] * L
stack = []

# output
for u in range(1, L):
    if not ids[u]:
        if not tarjan(u):
            print(-1)
            break
else:
    lamp = ['R'] * (k+1)
    for u in range(1, k+1):
        if scc_ids[u] < scc_ids[-u]:
            lamp[u] = 'B'
    print(''.join(lamp[1:]))