def solution(n, info):
    ans = 0
    ansp = [-1]
    
    def comb(i,r,v,vr,p):
        if i == 10:
            p += [r]
            nonlocal ans, ansp
            if ans == v - vr:
                ansp = max(ansp[::-1], p[::-1])[::-1]
            elif ans < v - vr:
                ans = v - vr
                ansp = p
            return
        if info[i] < r:
            comb(i+1, r-info[i]-1, v+10-i, vr, [*p]+[info[i]+1])
        if info[i]:
            comb(i+1 , r, v, vr+10-i, [*p]+[0])
        else:
            comb(i+1 , r, v, vr, [*p]+[0])
    comb(0, n, 0, 0, [])
    
    if not ans:
        return [-1]
    return ansp