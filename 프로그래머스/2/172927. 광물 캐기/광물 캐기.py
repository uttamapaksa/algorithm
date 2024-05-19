def solution(picks, minerals):
    dia = {"diamond": 1, "iron": 1, "stone": 1}
    iron = {"diamond": 5, "iron": 1, "stone": 1}
    stone = {"diamond": 25, "iron": 5, "stone": 1}
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    minerals = [[sum(dia[m] for m in ms), sum(iron[m] for m in ms), sum(stone[m] for m in ms)] for ms in minerals]
    
    d, i, s = picks
    memo = [[[1251] * (s+1) for _ in range(i+1)] for _ in range(d+1)]
    limit = min(sum(picks), len(minerals))
    ans = 1251
    def dfs(d, i, s, k, v):
        if memo[d][i][s] <= v:
            return
        memo[d][i][s] = v
        if k == limit:
            nonlocal ans
            ans = min(ans, v)
            return
        if d: dfs(d-1, i, s, k+1, v + minerals[k][0])
        if i: dfs(d, i-1, s, k+1, v + minerals[k][1])
        if s: dfs(d, i, s-1, k+1, v + minerals[k][2])        
    dfs(d, i, s, 0, 0)
    
    return ans
