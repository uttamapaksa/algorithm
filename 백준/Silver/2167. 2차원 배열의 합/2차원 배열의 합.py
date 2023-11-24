n, m = map(int, input().split())
arr = [[0] * (m+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (m+2)]

for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i][j] = arr[i][j] + arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]

for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    print(arr[r2][c2] - arr[r1-1][c2] - arr[r2][c1-1] + arr[r1-1][c1-1])
