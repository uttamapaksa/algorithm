def dfs(v):
    visit[v] = 1
    for w in graph[v]:
        if visit[w]: continue
        dfs(w)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)
ans = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    if visit[i]: continue
    ans += 1
    dfs(i)

print(ans)