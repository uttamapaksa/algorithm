T, W = map(int, input().split())
plum = [[0, 0]]  # tree, cnt
for _ in range(T):
    tree = int(input())
    if tree == plum[-1][0]:
        plum[-1][1] += 1
    else:
        plum.append([tree, 1])

dp = [0] * (W+1)
for tree, cnt in plum[1:]:
    if tree == 1:
        dp[0] += cnt
    for i in range(3-tree, W+1, 2):
        dp[i] = max(dp[i], dp[i-1]) + cnt

print(max(dp))