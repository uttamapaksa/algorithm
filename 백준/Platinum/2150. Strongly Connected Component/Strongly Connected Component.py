import sys; sys.setrecursionlimit(10**5)


def dfs(u):
    global id
    id += 1
    ids[u] = parent = id
    stack.append(u)

    for v in G[u]:
        if ids[v] == 0:
            parent = min(parent, dfs(v))
        elif not finished[v]:
            parent = min(parent, ids[v])

    if parent == ids[u]:
        scc = []
        while True:
            node = stack.pop()
            finished[node] = True
            scc.append(node)
            if node == u:
                break
        scc_list.append(sorted(scc))

    return parent


V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    A, B = map(int, input().split())
    G[A].append(B)

id = 0
ids = [0] * (V+1)
stack = []
finished = [False] * (V+1)
scc_list = []

for u in range(1, V+1):
    if not ids[u]:
        dfs(u)

print(len(scc_list))
for scc in sorted(scc_list):
    print(*scc, -1)