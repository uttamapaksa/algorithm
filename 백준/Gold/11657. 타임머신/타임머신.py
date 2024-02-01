def bellmanFord():
  INF = 5000001
  dist = [INF] * (N+1)
  dist[1] = 0
  
  for _ in range(1, N):
    for a, b, c in graph:
      if dist[a] != INF and dist[b] > dist[a] + c:
        dist[b] = dist[a] + c

  for _ in range(1, N):
    for a, b, c in graph:
      if dist[a] != INF and dist[b] > dist[a] + c:
        return -1

  ans = ""
  for i in range(2, N+1):
    ans += "-1\n" if dist[i] == INF else f"{dist[i]}\n"
  return ans


N, M = map(int, input().split())
graph = [(a, b, c) for _ in range(M) for a, b, c in [map(int, input().split())]]
print(bellmanFord())