import math


def find(x):
    if x != P[x]:
        P[x] = find(P[x])
    return P[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a < b: P[b] = a
    else: P[a] = b


# 모든 점들의 좌표 리스트
N = int(input())
P = [i for i in range(N)]
I = []
for _ in range(N):
    a, b = map(float, input().split())
    I.append((a, b))

# 모든 점들 간의 거리 리스트
G = []
for i in range(N-1):
    y1, x1 = I[i]
    for j in range(i+1, N):
        y2, x2 = I[j]
        v = round(math.sqrt((y2-y1) ** 2 + (x2-x1) ** 2), 4)
        G.append((v, i, j))
G.sort()

# 최소 신장 트리
ans = 0
for w, u, v in G:
    if find(u) != find(v):
        union(u, v)
        ans += w
print(ans)