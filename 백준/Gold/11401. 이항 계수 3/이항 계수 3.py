P = 1000000007
N, K = map(int, input().split())
K = max(K, N-K)

res = 1
if 0 < K < N:
    for i in range(N, K, -1):
        res = res * i % P
    mod = 1
    for i in range(1, N-K+1):
        mod = mod * i % P
    res = res * pow(mod, P-2, P) % P

print(res)