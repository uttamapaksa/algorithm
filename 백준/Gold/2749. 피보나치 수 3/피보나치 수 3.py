def fibo(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, (a + b) % M,
    return b


M = 10**6
p = 15 * 10**5
n = int(input())
print(fibo(n % p))