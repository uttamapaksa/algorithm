import sys; input = sys.stdin.readline
from heapq import heappop, heappush

N, M = int(input()), int(input())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append((w, v))
s, e = map(int, input().split())
D = [100000000] * (N+1)
D[s] = 0
q = [(D[s], s)]

while q:
    d, u = heappop(q)
    if u == e:
        print(D[e])
        break
    for w, v in G[u]:
        if D[v] > d + w:
            D[v] = d + w
            heappush(q, (D[v], v))