import sys; sys.setrecursionlimit(10001); input=sys.stdin.readline

def find(x):
    if x != P[x]:
        P[x] = find(P[x])
    return P[x]

V, E = map(int, input().split())
P = [i for i in range(V+1)]
G = []
for _ in range(E):
    s, e, w = map(int, input().split())
    G.append((w, s, e))
G.sort()

ans = 0
for w, s, e in G:
    a, b = find(s), find(e)
    if a != b: 
        ans += w
        if a > b:
            a, b = b, a
        P[b] = a

print(ans)