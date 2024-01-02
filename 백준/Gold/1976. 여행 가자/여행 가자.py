N, M = int(input()), int(input())
path = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
parent = list(range(N+1))
plan = list(map(int, input().split()))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a, b = find(x), find(y)
    if a < b: parent[b] = a
    else: parent[a] = b


for i in range(1, N+1):
    for j in range(1, N+1):
        if path[i][j]:
            union(i, j)


root = parent[plan[0]]
for city in set(plan):
    if root != parent[city]:
        print('NO')
        break
else:
    print('YES')