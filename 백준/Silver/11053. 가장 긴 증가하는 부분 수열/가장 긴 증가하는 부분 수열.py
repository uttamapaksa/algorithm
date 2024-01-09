N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    v = arr[i]
    for j in range(0, i):
        if arr[j] < v:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))