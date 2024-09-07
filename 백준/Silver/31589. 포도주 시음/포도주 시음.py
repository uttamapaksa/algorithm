N, K = map(int, input().split())
K = (K-1) // 2
T = sorted([*map(int, input().split())])
ans = sum(T[N-K-1:]) - sum(T[:K])
print(ans)