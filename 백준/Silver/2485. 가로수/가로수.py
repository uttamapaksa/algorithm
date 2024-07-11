from math import gcd
N = int(input())
a = [int(input()) for _ in range(N)]
a = [a[i+1]-a[i] for i in range(N-1)]
g = gcd(*a)
print(sum(v//g for v in a)-N+1)