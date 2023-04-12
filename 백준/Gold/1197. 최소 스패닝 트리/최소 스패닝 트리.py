def find(x):
    while x != P[x]:
        x = P[x]
    return x

def union(x, y):
    P[find(y)] = find(x)

V, E = map(int, input().split())
P = [i for i in range(V+1)]
G = []
MST = []

for _ in range(E):
    s, e, w = map(int, input().split())
    G.append((w, s, e))
G.sort()

cnt = 0
for w, s, e in G:
    if find(s) != find(e):
        cnt += 1
        MST.append((s, e, w))
        union(s, e)
        if cnt == V: break

ans = 0
for s, e, w in MST:
    ans += w
print(ans)