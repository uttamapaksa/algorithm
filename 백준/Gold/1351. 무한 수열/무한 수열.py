def sol(k):
    if k not in dp:
        dp[k]=sol(k//P)+sol(k//Q)
    return dp[k]

dp={0:1,1:2}
N,P,Q=map(int, input().split())
print(sol(N))