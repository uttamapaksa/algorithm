import sys; input = sys.stdin.readline
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
        dist = [25000000] * (N+1)
        visit = [0] * (N+1)
        count = [0] * (N+1)

        dist[start] = 0
        visit[start] = 1
        count[start] = 1
        q = deque([start])

        while q:
            s = q.popleft()
            visit[s] = 0
            for e, w in graph[s].items():

                if dist[e] > dist[s] + w:
                    dist[e] = dist[s] + w

                    if not visit[e]:
                        q.append(e)
                        visit[e] = 1
                        count[e] += 1

                        if count[e] == N:
                            return 1
        return 0

    for i in range(1, N+1):
        if bellman_ford(i):
            print('YES')
            break
    else:
        print('NO')