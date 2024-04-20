# find
def find(x):
    if P[x] != x:
        P[x] = find(P[x])
    return P[x]

# union
def union(w, x, y):
    a, b = find(x), find(y)
    if a == b:
        return 0
    if a > b:
        a, b = b, a
    P[b] = a
    return w

# static
xArr = []
yArr = []
zArr = []
answer = 0

# input
N = int(input())
P = list(range(N))
for planet in range(N):
    x, y, z = map(int, input().split())
    xArr.append((x, planet))
    yArr.append((y, planet))
    zArr.append((z, planet))
xArr.sort()
yArr.sort()
zArr.sort()

# diff heap
heap = []
for planet in range(N-1):
    # heappush w, u, v
    heap.append((xArr[planet+1][0] - xArr[planet][0], xArr[planet+1][1], xArr[planet][1]))
    heap.append((yArr[planet+1][0] - yArr[planet][0], yArr[planet+1][1], yArr[planet][1]))
    heap.append((zArr[planet+1][0] - zArr[planet][0], zArr[planet+1][1], zArr[planet][1]))
heap.sort(reverse=True)

# kruskal
answer = 0
while heap:
    w, u, v = heap.pop()
    answer += union(w, u, v)

# output
print(answer)