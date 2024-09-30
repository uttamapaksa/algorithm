from collections import deque

N, M, R = map(int, input().split())
visit = [-1] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visit[R] = 0
queue = deque([R])
while queue:
    u = queue.popleft()
    for v in graph[u]:
        if visit[v] != -1: continue
        visit[v] = visit[u] + 1
        queue.append(v)

print('\n'.join(map(str, visit[1:])))