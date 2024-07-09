from collections import deque

def solution(n, edges):
    G = [[] for _ in range(n+1)]
    for u, v in edges:
        G[u].append(v)
        G[v].append(u)
    dist = [[] for _ in range(n)]
    
    visit = [0] * (n+1)
    visit[1] = 1
    dist[0].append(1)
    Q = deque()
    Q.append((1, 0))
    
    while Q:
        u, d = Q.popleft()
        for v in G[u]:
            if visit[v]: continue
            visit[v] = 1
            dist[d+1].append(v)
            Q.append((v, d+1))
    
    return len(dist[d])