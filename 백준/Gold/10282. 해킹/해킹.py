from collections import deque

for _ in range(int(input())):
    n, d, c = map(int, input().split())

    G = [[] for _ in range(n + 1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        G[b].append((a, s))

    INF = int(1e9)

    queue = deque()
    queue.append(c)
    visited = [INF] * (n + 1)
    visited[c] = 0

    while queue:
        x = queue.popleft()

        for p, time in G[x]:
            if visited[p] > visited[x] + time:
                visited[p] = visited[x] + time
                queue.append(p)

    cnt = total = 0
    for time in visited:
        if time != INF:
            cnt += 1
            total = max(total, time)

    print(cnt, total)