import sys; input = sys.stdin.readline
from heapq import heappush, heappop

V, E = map(int, input().split())
S = int(input())
G = [{} for i in range(V+1)]
D = ['INF'] * (V+1)
visit = [0] * (V+1)
D[S] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    if v not in G[u]: G[u][v] = w
    else: G[u][v] = min(G[u][v], w)

q = []
heappush(q, (D[S], S))
while q:
    d, s = heappop(q)
    if visit[s]: continue
    visit[s] = 1
    for e in G[s]:
        if D[e] == 'INF':
            D[e] = D[s] + G[s][e]
            heappush(q, (D[e], e))
        else:
            if D[e] > D[s] + G[s][e]:
                D[e] = D[s] + G[s][e]
                heappush(q, (D[e], e))

for i in range(1, V+1):
    print(D[i])