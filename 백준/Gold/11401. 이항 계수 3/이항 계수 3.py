P = 1000000007
N, K = map(int, input().split())

if K == 0 or K == N:
    print(1)
else:
    fact = [1] * (N+1)
    for i in range(2, N+1):
        fact[i] = fact[i-1] * i % P
        
    NF = fact[N]
    IKF = pow(fact[K], P-2, P)
    INKF = pow(fact[N-K], P-2, P)
    print(NF * IKF % P * INKF % P)