from heapq import heappop, heappush

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    G = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        G[b].append((s, a))

    D = [10000001] * (n+1)
    D[c] = 0
    V = set()
    queue = [(0, c)]

    while queue:
        sw, s = heappop(queue)
        if s in V: continue
        V.add(s)
        for ew, e in G[s]:
            if D[e] > sw + ew:
                D[e] = sw + ew
                heappush(queue, (D[e], e))

    cnt = 0
    total = 0
    for time in D:
        if time != 10000001:
            cnt += 1
            total = max(total, time)

    print(cnt, total)