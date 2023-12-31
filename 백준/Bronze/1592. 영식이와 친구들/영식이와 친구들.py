N, M, L = map(int, input().split())
P = [0] * N
idx = ans = 0

P[idx] += 1
while P[idx] < M:
    if P[idx] % 2:
        idx = (idx + L) % N
    else:
        idx = (idx + N - L) % N
    P[idx] += 1
    ans += 1

print(ans)