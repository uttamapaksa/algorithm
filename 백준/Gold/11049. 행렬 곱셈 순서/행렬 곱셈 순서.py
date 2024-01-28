N = int(input())

row = [] # first num
col = [] # second num
for _ in range(N):
    a, b = map(int, input().split())
    row.append(a)
    col.append(b)

# cumulative value table
dp = [[float('inf')] * N for _ in range(N)] # [start, end]
for i in range(N):
    dp[i][i] = 0

# dp
for leng in range(1, N): # number of additions
    for start in range(N - leng):
        end = start + leng

        for mid in range(start, end):
            dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid+1][end] + row[start] * col[mid] * col[end])

# print from 0 to N
print(dp[0][N-1])