def solution(users, bans):
    n = len(users)
    m = len(bans)
    combs = []
    
    for ban in bans:
        k = len(ban)
        curr = []
        for i in range(n):
            user = users[i]
            if k != len(user):
                continue
            for j in range(k):
                if ban[j] == '*':
                    continue
                if ban[j] != user[j]:
                    break
            else:
                curr.append(i)
        if curr:
            combs.append(curr)
    
    k = len(combs)
    sets = set()
    def dfs(i, v):
        if i == k:
            sets.add(v)
            return
        for id in combs[i]:
            if v & (1 << id):
                continue
            dfs(i+1, v | (1 << id))
    dfs(0, 0)
    
    return len(sets)