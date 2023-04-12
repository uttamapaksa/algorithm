from collections import deque

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    graph = {i: {} for i in range(1, N+1)}

    for _ in range(M):
        s, e, w = map(int, input().split())
        if e not in graph[s]:
            graph[s][e] = w
        else:
            graph[s][e] = min(w, graph[s][e])
        if s not in graph[e]:
            graph[e][s] = w
        else:
            graph[e][s] = min(w, graph[e][s])

    for _ in range(W):
        s, e, w = map(int, input().split())
        if e not in graph[s]:
            graph[s][e] = -w
        else:
            graph[s][e] = min(-w, graph[s][e])

    def bellman_ford(start):
        n = len(graph)
        dist = {i: 250000000 for i in graph}
        dist[start] = 0
        visit = {i: 0 for i in graph}
        visit[start] = 1
        count = {i: 0 for i in graph}
        count[start] = 1

        queue = deque([start])
        while queue:
            u = queue.popleft()
            visit[u] = 0

            for v, w in graph[u].items():
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

                    if not visit[v]:
                        queue.append(v)
                        visit[v] = 1
                        count[v] += 1

                        if count[v] == n:
                            return 1
        return 0


    for i in graph:
        if bellman_ford(i):
            print('YES')
            break
    else:
        print('NO')