def find(x):
    if P[x] != x:
        P[x] = find(P[x])
    return P[x]


def union(x, y):
    a, b = find(x), find(y)
    if a == b:
        return
    if a > b:
        a, b = b, a
    P[b] = a
    candies[a] += candies[b]
    cnts[a] += cnts[b]


N, M, K = map(int, input().split())
candies = list(map(int, input().split()))
cnts = [1] * N
P = list(range(N))

for _ in range(M):
    u, v = map(int, input().split())
    union(u-1, v-1)

dp = [0] * K
P = {find(u) for u in P}
for root in P:
    cnt, candy = cnts[root], candies[root]
    for i in range(K-1, cnt-1, -1):
        dp[i] = max(dp[i], dp[i-cnt] + candy)

print(dp[K-1])