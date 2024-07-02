def solution(gems):
    n = len(gems)
    m = len(set(gems))
    diff = 100001
    s = e = 0
    ss = ee = 0
    
    cnt = {}
    while e < n:
        cnt[gems[e]] = cnt.get(gems[e], 0) + 1
        while len(cnt) == m:
            if diff > e - s:
                diff = e - s
                ss, ee = s, e 
            cnt[gems[s]] -= 1
            if not cnt[gems[s]]:
                del cnt[gems[s]]
            s += 1
        e += 1
                
    return [ss+1, ee+1]