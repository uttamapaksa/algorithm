def to_sort(graph, degree, known):
    stack = [i for i in range(1, N+1) if not degree[i]]
    while stack:
        u = stack.pop()
        for v in graph[u]:
            known[v] |= known[u]
            degree[v] -= 1
            if not degree[v]:
                stack.append(v)


N, M = map(int, input().split())
parents = [{i} for i in range(N+1)]
children = [{i} for i in range(N+1)]
ingraph = [[] for _ in range(N+1)]
outgraph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
outdegree = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    ingraph[a].append(b)
    indegree[b] += 1
    outgraph[b].append(a)
    outdegree[a] += 1

to_sort(ingraph, indegree, children)
to_sort(outgraph, outdegree, parents)

ans = 0
for i in range(1, N+1):
    if len(children[i] | parents[i]) == N:
        ans += 1
print(ans)