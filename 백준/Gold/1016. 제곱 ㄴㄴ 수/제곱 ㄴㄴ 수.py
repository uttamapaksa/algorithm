mn, mx = map(int, input().split())
prime = set(range(mn, mx+1))

for i in range(2, int(mx**0.5)+1):
    sqr = i**2
    for div in range((mn-1) // sqr + 1, mx // sqr + 1):
        prime.discard(sqr * div)

print(len(prime))