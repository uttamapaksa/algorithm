N, M, S = map(int, input().split())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)] + [[S, S]]
arr.sort()

ans = -1
for i in range(N+1):
    if arr[i+1][0] - sum(arr[i]) >= M:
        ans = sum(arr[i])
        break

print(ans)