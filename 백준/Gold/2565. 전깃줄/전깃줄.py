N = int(input())
arr = {a: b for _ in range(N) for a, b in [map(int, input().split())]}
arr = sorted(arr.items())

dp = [1] * N
for i in range(N):
    for j in range(i+1, N):
        if arr[j][1] > arr[i][1]:
            dp[j] = max(dp[j], dp[i]+1)

print(N-max(dp))