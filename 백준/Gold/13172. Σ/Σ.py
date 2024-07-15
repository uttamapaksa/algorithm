MOD = 1000000007
count = 0
for _ in range(int(input())):
    N, S = map(int, input().split())
    IN = pow(N, MOD-2, MOD)
    count = (count + IN * S) % MOD
print(count)