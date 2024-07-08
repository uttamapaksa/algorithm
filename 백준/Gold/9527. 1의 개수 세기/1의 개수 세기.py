A, B = map(int, input().split())
abin, bbin = bin(A-1)[2:], bin(B)[2:]
alen, blen = len(abin), len(bbin)

dp = [0, 1]
for i in range(2, blen+1):
    dp.append(2*dp[i-1] + 2**(i-1))

ans = 0
for i in range(blen-1):
    if bbin[i] == '1':
        ans += dp[blen-i-1]
        ans += int(bbin[i+1:], 2) + 1
ans += int(bbin[-1])
for i in range(alen-1):
    if abin[i] == '1':
        ans -= dp[alen-i-1]
        ans -= int(abin[i+1:], 2) + 1
ans -= int(abin[-1])

print(ans)