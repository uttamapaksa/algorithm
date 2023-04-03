n = int(input())
dp = {0: n}
maxtmp = [n]
maxcnt = 1

for i in range(n, 0, -1):
    dp[1] = i
    tmp = [n]
    cnt = 1

    j = 1
    while dp[j] >= 0:
        tmp.append(dp[j])
        cnt += 1
        j += 1
        dp[j] = dp[j-2] - dp[j-1]

    if cnt > maxcnt:
        maxtmp = tmp
        maxcnt = cnt

print(maxcnt)
print(*maxtmp)