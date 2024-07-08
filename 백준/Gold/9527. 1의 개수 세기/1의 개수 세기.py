def count1(n):
    num = bin(n)[2:]
    N = len(num)

    res = 0
    for i in range(N-1):
        if num[i] == '1':
            res += dp[N-i-1]
            res += int(num[i+1:], 2) + 1
    res += int(num[-1])
    return res


A, B = map(int, input().split())
dp = [0, 1]
for i in range(2, len(bin(B)[2:])+1):
    dp.append(2*dp[i-1] + 2**(i-1))

print(count1(B) - count1(A-1))