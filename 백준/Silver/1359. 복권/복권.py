N, M, K = map(int, input().split())

def combination(n, m):
    if n < m:
        return 0
    if m > n - m:
        m = n - m
    res = 1
    for i in range(m):
        res *= n - i
        res //= i + 1
    return res

ans = 0
for k in range(K, M+1):
    ans += combination(M, k) * combination(N-M, M-k) / combination(N, M)
print(ans)