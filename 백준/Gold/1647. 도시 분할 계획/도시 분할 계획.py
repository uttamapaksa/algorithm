N, M = map(int, input().split())
P = [i for i in range(N+1)]
G = []

for _ in range(M):
    G.append(tuple(map(int, input().split())))
G.sort(key=lambda x: x[2])

def find(x):
    if P[x] != x:
        P[x] = find(P[x])
    return P[x]

sums = maxs = cnt = 0
for u, v, w in G:
    if cnt == N-1: break
    u, v = find(u), find(v)
    if u != v:
        if u < v: P[v] = u
        else: P[u] = v
        cnt += 1
        sums += w
        maxs = max(maxs, w)

print(sums - maxs)