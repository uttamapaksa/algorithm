import sys; input = sys.stdin.readline

def find(x):
    if x != P[x]:
        P[x] = find(P[x])
    return P[x]

while True:
    m, n = map(int, input().split())
    if not m and not n:
        break
    P = list(range(m))
    G = [tuple(map(int, input().split())) for _ in range(n)]
    G.sort(key=lambda x: x[2])

    saved = 0
    for u, v, w in G:
        a, b = find(u), find(v)
        if a == b:
            saved += w
        elif a < b:
            P[b] = a
        else:
            P[a] = b
    print(saved)