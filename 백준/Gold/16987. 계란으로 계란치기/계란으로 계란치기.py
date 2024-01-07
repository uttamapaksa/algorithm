N = int(input())
egg = [list(map(int, input().split())) for _ in range(N)]
broken = [0] * N
ans = 0


def dfs(v, k):
    global ans
    if ans >= v + (N-k) * 2: # pruning
        return 
    if k == N:
        ans = max(ans, v)
        return
    if broken[k]: # pass
        dfs(v, k+1)
        return

    # something exists to break
    for i in range(N):
        if not broken[i] and i != k:
            break
    else:
        ans = max(ans, v)
        return

    # backtracking
    for i in range(N):
        if broken[i] or i == k: continue
        egg[k][0] -= egg[i][1]
        egg[i][0] -= egg[k][1]
        if egg[k][0] <= 0: broken[k] = 1
        if egg[i][0] <= 0: broken[i] = 1
        dfs(v + broken[k] + broken[i], k+1)
        egg[k][0] += egg[i][1]
        egg[i][0] += egg[k][1]
        if egg[k][0] > 0: broken[k] = 0
        if egg[i][0] > 0: broken[i] = 0


dfs(0, 0)
print(ans)