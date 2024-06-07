n = int(input())
arr = [*map(int, input().split())]
dp = [[v, 0] for v in arr]  # not deleted, deleted

for i in range(n-2, -1, -1):
    # max(curr, curr + max_sum)
    dp[i][0] = max(dp[i][0], arr[i] + dp[i+1][0])
    # max(delete curr, curr + deleted_max_sum)
    dp[i][1] = max(dp[i+1][0], arr[i] + dp[i+1][1])
# last one only
dp[n-1][1] = arr[n-1]

print(max(max(v) for v in dp))