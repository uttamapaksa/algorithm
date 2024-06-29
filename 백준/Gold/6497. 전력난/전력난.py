def find(x):
    if x != P[x]:
        P[x] = find(P[x])
    return P[x]

def union(x, y):
    a, b = find(x), find(y)
    if a == b:
        return 0
    if a > b:
        a, b = b, a
    P[b] = a
    return 1

ans = []
while True:
    m, n = map(int, input().split())
    if not m and not n:
        print('\n'.join(ans))
        break
    
    P = list(range(m))
    G = []
    for _ in range(n):
        u, v, w = map(int, input().split())
        G.append((w, u, v))
    G.sort()

    saved = 0
    for w, u, v, in G:
        if not union(u, v):
            saved += w
    ans.append(str(saved))