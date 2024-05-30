from heapq import heappush, heappop

N, M = map(int, input().split())

G = {i: {} for i in range(1, N+1)}
for _ in range(M):
    a, b, c = map(int, input().split())
    if a not in G[b]:
        G[a][b] = c
        G[b][a] = c
    else:
        G[a][b] = max(G[a][b], c)
        G[b][a] = max(G[b][a], c)

S, E = map(int, input().split())
D = [0] * (N+1)
D[S] = float('inf')
heap = [(-D[S], S)]

while heap:
    d, u = heappop(heap)
    d = -d
    if D[u] > d: continue
    for v, w in G[u].items():
        if D[v] < min(d, w):
            D[v] = min(d, w)
            heappush(heap, (-D[v], v))

print(D[E])