import sys; input = sys.stdin.readline

def find(x):
    if P[x] != x:
        P[x] = find(P[x])
    return P[x]

V, E = map(int, input().split())
P = [i for i in range(V+1)]
tmp = [{} for _ in range(V+1)]
G = []
MST = []

for _ in range(E):
    s, e, w = map(int, input().split())
    if s > e: s, e = e, s
    if e not in tmp[s]: tmp[s][e] = w
    else: tmp[s][e] = min(tmp[s][e], w)

for s in range(len(tmp)):
    for e, w in tmp[s].items():
        G.append((w, s, e))
G.sort()

sums = 0
for w, s, e in G:
    a, b = find(s), find(e)
    if a != b:
        P[b] = a
        sums += w
        MST.append(w)

print(sums - max(MST))