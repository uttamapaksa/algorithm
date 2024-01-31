from heapq import heappush, heappop

def daijkstra(s):
    dist = [2000001] * (n+1)
    dist[s] = 0
    priority_queue = []
    heappush(priority_queue, (dist[s], s))

    while priority_queue:
        d, u = heappop(priority_queue)
        if dist[u] < d: continue

        for w, v in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heappush(priority_queue, (dist[v], v))
                  
    return dist


N = int(input())
ans = ""
for _ in range(N):
    n, m ,t = map(int, input().split())
    s, g ,h = map(int, input().split())

    graph = {i: [] for i in range(1, n+1)}
    for _ in range(m):
      a, b, d = map(int, input().split())
      graph[a].append((d, b))
      graph[b].append((d, a))

    destinations = sorted(int(input()) for _ in range(t))
    dists = daijkstra(s)
    distg = daijkstra(g)
    disth = daijkstra(h)
    for ww, v in graph[g]:
       if v == h:
          w = ww
          break
       
    for x in destinations:
       if dists[x] == dists[g] + w + disth[x] or dists[x] == dists[h] + w + distg[x]:
          ans += f'{x} '
    ans += "\n"

print(ans)