def find(x):
    if P[x] != x:
        P[x] = find(P[x])
    return P[x]

def union(x, y):
    a, b = find(x), find(y)
    if a > b:
        a, b = b, a
    P[b] = a

N = int(input())
M = int(input())
P = list(range(N))

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a-1, b-1))
edges.sort()

ans = 0
for w, u, v in edges:
    if find(u) == find(v): continue
    union(u, v)
    ans += w

print(ans)