def solution(users, emoticons):
    n = len(emoticons)
    m = len(users)
    cost = [0] * m
    ans = [0, 0]
    
    def dfs(k):
        if k == n:
            nonlocal ans
            curr = [0, 0]
            for i in range(m):
                if cost[i] >= users[i][1]:
                    curr[0] += 1
                else:
                    curr[1] += cost[i]
            ans = max(ans, curr)
            return
        for per in (10, 20, 30, 40):
            val = emoticons[k] * (100 - per) / 100
            for i in range(m):
                if users[i][0] <= per:
                    cost[i] += val
            dfs(k+1)
            for i in range(m):
                if users[i][0] <= per:
                    cost[i] -= val
    dfs(0)
            
    return ans