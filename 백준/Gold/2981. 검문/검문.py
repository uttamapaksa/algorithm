from math import gcd

N = int(input())
arr = sorted(int(input()) for _ in range(N))
arr = [arr[i+1] - arr[i] for i in range(N-1)]
g = gcd(*arr)

ans = {g}
for i in range(2, int(g**0.5)+1):
    if not g % i:
        ans.add(i)
        ans.add(g//i)

print(*sorted(ans))