N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
E = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    E[b] += 1

Q = []
for i in range(1, N+1):
    if not E[i]:
        Q.append(i)

ans = []
while Q:
    v = Q.pop()
    ans.append(v)
    for w in G[v]:
        E[w] -= 1
        if not E[w]:
            Q.append(w)

print(*ans)