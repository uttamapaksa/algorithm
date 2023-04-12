A, B = [0] + [*input()], [0] + [*input()]
a, b = len(A), len(B)
dp = [[0] * (b+1) for _ in range(a+1)]

for i in range(1, a):
    for j in range(1, b):
        if A[i] == B[j]: dp[i][j] = dp[i-1][j-1] + 1
        else: dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[a-1][b-1])