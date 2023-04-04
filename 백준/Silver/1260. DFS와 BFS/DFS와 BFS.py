from collections import deque

def DFS(v):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            DFS(w)
    return visited

def BFS(v):
    visited = []
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.append(v)
            queue.extend(graph[v])
    return visited

V, E, v = map(int, input().split())
graph = {i: [] for i in range(1, V+1)}
visited = []

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for lst in graph:
    graph[lst].sort()
    
print(*DFS(v))
print(*BFS(v))