import sys; sys.setrecursionlimit(10**5)


def dfs(u):
    global id, scc_id
    id += 1
    ids[u] = par = id
    stack.append(u)

    for v in G[u]:
        if not ids[v]:
            par = min(par, dfs(v))
        elif not finished[v]:
            par = min(par, ids[v])

    if par == ids[u]:
        scc_id += 1
        indegrees[scc_id] = 0
        while 1:
            v = stack.pop()
            finished[v] = 1
            scc_ids[v] = scc_id
            if v == u:
                break
    
    return par


for _ in range(int(input())):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    V = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
    
    id = 0
    ids = [0] * (N+1)
    stack = []
    finished = [0] * (N+1)
    scc_id = 0
    scc_ids = [0] * (N+1)
    indegrees = {}

    for u in range(1, N+1):
        if not ids[u]:
            dfs(u)

    for u in range(1, N+1):
        for v in G[u]:
            if scc_ids[u] != scc_ids[v]:
                indegrees[scc_ids[v]] += 1

    ans = 0
    for id in indegrees:
        if not indegrees[id]:
            ans += 1
    print(ans)