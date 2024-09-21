N = input()
L = len(N)

ans = (int(N) - 10**(L-1) + 1) * L
for i in range(1, L):
    ans += 9*10**(i-1) * i

print(ans)