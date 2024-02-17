def dfs(u):
    visit[u] = 1
    for v in graph[u]:
        if visit[v]: continue
        dfs(v)
        dp[u][0] += dp[v][1]  # add
        dp[u][2] += dp[v][3]  # add_path
        dp[u][1] += dp[v][0] if dp[v][0] > dp[v][1] else dp[v][1]  # pass
        dp[u][3] += dp[v][2] if dp[v][0] > dp[v][1] else dp[v][3]  # pass_path


N, W = int(input()), list(map(int, input().split()))
dp = [[W[i-1], 0, [i], []] for i in range(N+1)]  # add, pass, add_path, pass_path
visit = [0] * (N+1)
graph = {i: [] for i in range(1, N+1)}
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)
idx = int(dp[1][0] < dp[1][1])
print(f"{dp[1][idx]}\n{' '.join(map(str, sorted(dp[1][idx+2])))}")