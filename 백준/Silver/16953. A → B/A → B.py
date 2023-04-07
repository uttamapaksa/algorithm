A, B = map(int, input().split())
dp = {B: 1}
for i in range(B, A-1, -1):
    if i not in dp: continue
    if not i % 2:
        n = i // 2
        if n >= A:
            if n in dp: dp[n] = min(dp[n], dp[i] + 1)
            else: dp[n] = dp[i] + 1
    elif i % 10 == 1:
        n = i // 10
        if n >= A:
            if n in dp: dp[n] = min(dp[n], dp[i] + 1)
            else: dp[n] = dp[i] + 1
if A in dp: print(dp[A])
else: print(-1)