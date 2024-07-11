strs = input()
N = len(strs)

dp = [[0] * 26 for _ in range(N+1)]
for i in range(N):
    for j in range(26):
        dp[i][j] += dp[i-1][j]
    dp[i][ord(strs[i])-97] += 1

ans = []
for _ in range(int(input())):
    a, l, r = input().split()
    a, l, r = ord(a)-97, int(l), int(r)
    ans.append(str(dp[r][a] - dp[l-1][a]))

print('\n'.join(ans))