N, K = map(int, input().split())
ans = 0
while bin(N).count('1') > K:
    add = N & -N
    N += add
    ans += add
print(ans)