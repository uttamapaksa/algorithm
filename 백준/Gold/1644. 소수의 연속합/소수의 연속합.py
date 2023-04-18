N = int(input())
prime = set(range(2, N+1))

for i in range(2, N+1):
    for j in range(2, int(i ** 0.5) + 1):
        if not i % j:
            prime.discard(i)
            break

l = len(prime)
prime = list(prime)
ans = 0
for i in range(l):
    sums = 0
    for j in range(i, l):
        sums += prime[j]
        if sums >= N:
            if sums == N:
                ans += 1
            break

print(ans)