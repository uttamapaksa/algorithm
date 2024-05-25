def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))
    
    ans = 0
    missile = -1
    for target in targets:
        s, e = target
        if missile < s:
            ans += 1
            missile = e - 0.5
            
    return ans