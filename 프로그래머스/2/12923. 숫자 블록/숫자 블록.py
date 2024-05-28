def solution(begin, end):
    INF = 10000000
    ps = {i: 1 for i in range(begin, end+1)}
    
    for v in ps.keys():
        for i in range(2, int(v**0.5) + 1):
            if not v % i:
                ps[v] = max(ps[v], i)
                if v//i <= INF:
                    ps[v] = max(ps[v], v//i)
                
    if begin == 1:
        ps[1] = 0
    return [*ps.values()]