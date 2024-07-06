import sys; sys.setrecursionlimit(10**5); input=sys.stdin.readline


def dfs(u):
    global id
    id += 1
    ids[u] = par = id
    stack.append(u)
    
    for v in G[u]:
        if not ids[v]:
            par = min(par, dfs(v))
        elif not scc_ids[v]:
            par = min(par, ids[v])

    if par == ids[u]:
        zero_indegrees.add(par)
        while 1:
            v = stack.pop()
            scc_ids[v] = par
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
    scc_ids = [0] * (N+1)
    stack = []
    zero_indegrees = set()

    for u in range(1, N+1):
        if not ids[u]:
            dfs(u)

    for u in range(1, N+1):
        for v in G[u]:
            if scc_ids[u] != scc_ids[v]:
                zero_indegrees.discard(scc_ids[v])

    print(len(zero_indegrees))