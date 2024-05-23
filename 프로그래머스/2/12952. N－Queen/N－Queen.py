def solution(n):
    arr = [[0] * n for _ in range(n)]
    ans = 0
    
    rdv = [0] * (2*n)
    ldv = [0] * (2*n)
    cv = [0] * n
    
    def nqueen(r):
        if r == n:
            nonlocal ans
            ans += 1
            return        
        for c in range(n):
            if rdv[r-c] or ldv[r+c] or cv[c]: continue
            rdv[r-c] = 1; ldv[r+c] = 1; cv[c] = 1
            nqueen(r+1)
            rdv[r-c] = 0; ldv[r+c] = 0; cv[c] = 0
    nqueen(0)
    
    return ans