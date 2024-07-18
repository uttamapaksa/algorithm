import sys; sys.setrecursionlimit(10**5)

def dfs(u):
    global id; id += 1
    ids[u] = par = id
    stack.append(u)

    for v in G[u]:
        if not ids[v]:
            par = min(par, dfs(v))
        elif not scc_ids[v]:
            par = min(par, ids[v])

    if par == ids[u]:
        global scc_id; scc_id += 1
        scc[scc_id] = []
        while 1:
            v = stack.pop()
            scc_ids[v] = scc_id
            scc[scc_id].append(v)
            if v == u:
                break

    return par


tc = int(input())
for t in range(tc):
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map (int, input().split())
        G[a].append(b)
    if t != tc-1:
        input()

    id = 0
    ids = [0] * N
    scc_id = 0
    scc_ids = [0] * N
    scc = {}
    stack = []
    for u in range(N):
        if ids[u]: continue
        dfs(u)

    for u in range(N):
        for v in G[u]:
            if scc_ids[u] != scc_ids[v] and scc_ids[v] in scc:
                del scc[scc_ids[v]]
    
    if len(scc) > 1:
        print("Confused")
    elif len(scc) == 1:
        print(*sorted([*scc.values()][0]), sep='\n')
    else:
        print(*tuple(i for i in range(N)), sep='\n')
    print()