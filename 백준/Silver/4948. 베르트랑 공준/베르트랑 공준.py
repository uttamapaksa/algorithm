from bisect import bisect_left

prime = set(range(2, 246913))
for i in range(2, 497):
    for j in range(i*i, 246913, i):
        prime.discard(j)
prime = sorted(prime)

while i:
    n = int(input())
    if not n: break
    l, r = bisect_left(prime, n+1), bisect_left(prime, 2*n+1)
    print(r-l)