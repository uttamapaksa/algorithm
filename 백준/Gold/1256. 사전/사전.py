from math import comb

n, m, k = map(int, input().split())
t = n+m
if comb(n+m, n) < k:
    print(-1)
else:
    r = ["a"] * (n+m)
    for i in range(t):
        cnt = comb(t-i-1, m)
        if k > cnt:
            k -= cnt
            m -= 1
            r[i] = "z"
    print("".join(r))
