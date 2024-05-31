A = "_" + input()
B = "_" + input()
N, M = len(A), len(B)

dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N):
    for j in range(1, M):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1

ans = max(max(row) for row in dp)
print(ans)