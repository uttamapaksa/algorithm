from heapq import heappush, heappop

n, m = int(input()), int(input())
arr = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    arr[u][v] = min(arr[u][v], w)

s, e = map(int, input().split())
dist = [float('inf')] * (n+1)
dist[s] = 0
heap = []
heappush(heap, (0, s))

parent = {}
while heap:
    w, u = heappop(heap)
    if dist[u] < w: continue
    if u == e: break
    for v in range(1, n+1):
        if dist[v] > w + arr[u][v]:
            dist[v] = w + arr[u][v]
            parent[v] = u
            heappush(heap, (dist[v], v))

print(dist[e])
path = [e]
while e != s:
    e = parent[e]
    path = [e] + path
print(len(path))
print(*path)