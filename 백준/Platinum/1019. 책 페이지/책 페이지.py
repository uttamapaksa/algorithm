def sol():
    # one
    if K == 1:
        for n in range(1, int(N)+1):
            ans[n] = 1
        return
    # first
    ans[0] += dp[K-1][0]
    for i in range(1, 10):
        ans[i] += dp[K-1][1]
    for n in range(1, int(N[0])):
        ans[n] += 10 ** (K-1)
        for j in range(10):
            ans[j] += 10 ** (K-2) * (K-1)
    ans[int(N[0])] += int(N[1:]) + 1
    # middle
    for i in range(1, K-1):
        d = K-i
        for n in range(int(N[i])):
            ans[n] += 10 ** (d-1)
            for j in range(10):
                ans[j] += 10 ** (d-2) * (d-1)
        ans[int(N[i])] += int(N[i+1:]) + 1
    # last
    for n in range(0, int(N[K-1])+1):
        ans[n] += 1

dp = [0,[0,1],[9,20],[189,300],[2889,4000],[38889,50000],[488889,600000],[5888889,7000000],[68888889,80000000],[788888889,900000000]]
ans = [0] * 10
N = input()
K = len(N)
sol()
print(*ans)