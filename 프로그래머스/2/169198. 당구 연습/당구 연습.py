def path(m, n, sx, sy, ex, ey):
    res = 1000001
    if sx != ex or sy > ey:  # north
        res = min(res, abs(ex-sx) ** 2 + (n-sy+n-ey) ** 2)
    if sx != ex or sy < ey:  # south
        res = min(res, abs(ex-sx) ** 2 + (sy+ey) ** 2)
    if sy != ey or sx < ex:  # east
        res = min(res, abs(ey-sy) ** 2 + (sx+ex) ** 2)
    if sy != ey or sx > ex:  # west
        res = min(res, abs(ey-sy) ** 2 + (m-sx+m-ex) ** 2)
    return res
    
    
def solution(m, n, sx, sy, balls):
    answer = [path(m, n, sx, sy, *ball) for ball in balls]
    return answer