def solution(genres, plays):
    n = len(plays)
    lst = {}
    cnt = {}
    
    for i in range(n):
        g, p = genres[i], plays[i]
        if g not in lst: lst[g] = [(p, i)]
        else: lst[g].append((p, i))
        cnt[g] = cnt.get(g, 0) + p
    
    ans = []
    for g, c in sorted(cnt.items(), key=lambda x: -x[1]):
        lst[g].sort(key=lambda x: (-x[0], x[1]))
        ans.append(lst[g][0][1])
        if len(lst[g]) > 1:
            ans.append(lst[g][1][1])
    
    return ans 