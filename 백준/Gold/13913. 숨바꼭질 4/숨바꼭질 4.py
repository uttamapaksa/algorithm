# BFS

from collections import deque

N, K = map(int, input().split())
visit = [-1] * 100001
visit[N] = -2 # start point
q = deque()
q.append((0, N))

while q:
    cnt, s = q.popleft()
    # find it!
    if s == K:
        break
    # -1
    ns = s-1
    if ns >= 0 and visit[ns] == -1:
        visit[ns] = s
        q.append((cnt+1, ns))
    # +1, ×2
    if s < K:
        for ns in (s*2, s+1):
            if ns <= 100000 and visit[ns] == -1:
                visit[ns] = s
                q.append((cnt+1, ns))

# trace previous visit
path = deque()
while s != -2:
    path.appendleft(s)
    s = visit[s]

print(cnt)
print(*path)