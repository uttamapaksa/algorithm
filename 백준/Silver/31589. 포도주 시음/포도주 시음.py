N, K = map(int, input().split())
K = (K-1) // 2
T = [*map(int, input().split())]
T.sort()

ans = 0
for i in range(K):
    ans -= T[i]
for i in range(N-K-1, N):
    ans += T[i]
print(ans)