for _ in range(int(input())):
    N, M = map(int, input().split())
    if not N: print(0)
    else:
        ans = 1
        for i in range(N):
            ans *= (M-i)
        for i in range(1, N+1):
            ans //= i
        print(int(ans))