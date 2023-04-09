from heapq import heappop,heappush

N, K = map(int, input().split())
visit = [0] * 100001
visit[N] = 1
q = [(0, N)]

while q:
    cnt, s = heappop(q)
    if s == K:
        break
    if s < K:
        i = s * 2
        if 0 < i <= 100000 and not visit[i]:
            visit[i] = 1
            heappush(q, (cnt, i))
        i = s + 1
        if i <= 100000 and not visit[i]:
            visit[i] = 1
            heappush(q, (cnt + 1, i))
    if s > 0:
        i = s - 1
        if not visit[i]:
            visit[i] = 1
            heappush(q, (cnt + 1, i))

print(cnt)