from collections import deque

N, M, R = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
for u in G:
    u.sort(reverse=True)

Q = deque()
Q.append(R)
visit = [0] * (N+1)
order = 1
visit[R] = order

while Q:
    u = Q.popleft()
    for v in G[u]:
        if visit[v]: continue
        Q.append(v)
        order += 1
        visit[v] = order
        
print(*visit[1:], sep='\n')