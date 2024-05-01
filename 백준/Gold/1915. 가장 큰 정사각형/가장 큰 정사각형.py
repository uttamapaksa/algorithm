N, M = map(int, input().split())
arr = [[0] * (M+1)] + [[0] + [*map(int, [*input()])] for _ in range(N)]
ans = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j]:
            arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
            ans = max(ans, arr[i][j])

print(ans ** 2)