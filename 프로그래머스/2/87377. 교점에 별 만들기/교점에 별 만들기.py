def solution(line):
    n = len(line)
    INF = float('inf')
    mnx, mny, mxx, mxy = INF, INF, -INF, -INF
    stars = []
    
    for i in range(n-1):
        a, b, e = line[i]
        for j in range(i+1, n):
            c, d, f = line[j]
            denominator = a*d-b*c
            if not denominator: continue
            nx = (b*f-e*d) / denominator
            ny = (e*c-a*f) / denominator
            if int(nx) != nx or int(ny) != ny: continue
            nx, ny = int(nx), int(ny)
            stars.append((nx, ny))
            mnx, mny, mxx, mxy = min(mnx, nx), min(mny, ny), max(mxx, nx), max(mxy, ny)
    
    ans = [["."] * (mxx-mnx+1) for _ in range(mxy-mny+1)]
    for nx, ny in stars:
        ans[mxy-ny][nx-mnx] = '*'
    ans = ["".join(row) for row in ans]
    
    return ans