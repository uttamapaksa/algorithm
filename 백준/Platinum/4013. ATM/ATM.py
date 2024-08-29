# import
import sys; sys.setrecursionlimit(1000000); input=sys.stdin.readline
from collections import deque

# input
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
C = [0] + [int(input()) for _ in range(N)]
S, _ = map(int, input().split())

# SCC. Tarjan
def dfs(u):
    global id, scc_id
    id += 1
    ids[u] = par = id
    stack.append(u)
    for v in G[u]:
        if not ids[v]:
            par = min(par, dfs(v))
        elif not scc_ids[v]:
            par = min(par, ids[v])
    if par == ids[u]:
        scc_id += 1
        while 1:
            v = stack.pop()
            scc_ids[v] = scc_id
            if u == v:
                break
    return par

id = 0
ids = [0] * (N+1)
scc_id = 0
scc_ids = [0] * (N+1)
stack = []
for u in range(1, N+1):
    if not ids[u]:
        dfs(u)

# DAG
scc_graph = [set() for _ in range(scc_id+1)]
scc_cost = [0] * (scc_id+1)
indegree = [0] * (scc_id+1)
for u in range(1, N+1):
    scc_cost[scc_ids[u]] += C[u]
    for v in G[u]:
        if scc_ids[u] == scc_ids[v]: continue
        if scc_ids[v] in scc_graph[scc_ids[u]]: continue
        scc_graph[scc_ids[u]].add(scc_ids[v])
        indegree[scc_ids[v]] += 1
outback = [0] * (scc_id+1)
for u in map(int, input().split()):
    outback[scc_ids[u]] = 1

# Topological sort
S = scc_ids[S]
C = [0] * (scc_id+1)
C[S] = scc_cost[S]
can_go = [0] * (scc_id+1)
can_go[S] = 1
Q = deque()
for u in range(1, scc_id+1):
    if not indegree[u]:
        Q.append(u)
while Q:
    u = Q.popleft()
    for v in scc_graph[u]:
        indegree[v] -= 1
        if not indegree[v]: 
            Q.append(v)
        if can_go[u]:
            can_go[v] = 1
            C[v] = max(C[v], C[u] + scc_cost[v])

# output
ans = 0
for u in range(1, scc_id+1):
    if outback[u] and ans < C[u]:
        ans = C[u]
print(ans)