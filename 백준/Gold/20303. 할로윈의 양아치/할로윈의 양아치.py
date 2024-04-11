def find(x):
    if P[x] != x:
        P[x] = find(P[x])
    return P[x]


def union(x, y):
    a, b = find(x), find(y)
    if a == b:
        return 
    if a < b:
        P[b] = a
    else:
        P[a] = b


N, M, K = map(int, input().split())
candies = list(map(int, input().split()))
cnts = [1] * N
P = list(range(N))

for _ in range(M):
    u, v = map(int, input().split())
    union(u-1, v-1)

for u in range(N):
    root = find(u)
    if u != root:
        candies[root] += candies[u]
        cnts[root] += cnts[u]

cnt_candy = []
for root in set(P):
    cnt_candy.append((cnts[root], candies[root]))

dp = [0] * K
for cnt, candy in cnt_candy:
    for i in range(K-1, cnt-1, -1):
        dp[i] = max(dp[i], dp[i-cnt] + candy)

print(dp[K-1])