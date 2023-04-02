from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
for i in range(1, N + 1):
    bacon = 0
    visit = [0] * (N + 1)
    visit[i] = 1
    q = deque([(i, 1)])
    while q:
        v, k = q.popleft()
        for w in graph[v]:
            if visit[w]: continue
            visit[w] = 1
            bacon += k
            q.append((w, k + 1))
    if ans:
        if bacon < mins:
            mins = bacon
            ans = i
    else:
        mins = bacon
        ans = i

print(ans)