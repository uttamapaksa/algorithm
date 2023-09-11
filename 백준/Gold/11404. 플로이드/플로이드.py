import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = 10e9
arr = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    arr[i][i] = 0

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if arr[a][b] > c:
        arr[a][b] = c

for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            if arr[a][b] > arr[a][k] + arr[k][b]:
                arr[a][b] = arr[a][k] + arr[k][b]
                
for i in range(n+1):
    for j in range(n+1):
        if arr[i][j] == INF:
            arr[i][j] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i][j], end=' ')
    print('')