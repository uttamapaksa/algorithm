from heapq import heappop, heappush

n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

D = [float('inf')] * (n+1)
D[1] = 0
H = [(D[1], 1)]
while H:
    w, u = heappop(H)
    if D[u] < w: continue
    for v, d in G[u]:
        if D[v] > w + d:
            D[v] = w + d
            heappush(H, (D[v], v))

print(D[n])
