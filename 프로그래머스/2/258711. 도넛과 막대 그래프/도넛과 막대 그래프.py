def solution(edges):
    ans = [0, 0, 0]
    g = {}
    rg = {}
    for s, e in edges:
        if s in g:
            g[s].append(e)
        else:
            g[s] = [e]
        if e in rg:
            rg[e].append(s)
        else:
            rg[e] = [s]

    start = 0
    for key in g:
        if len(g[key]) > 1 and key not in rg:
            start = key
            break
            
    sg = g[start]
    del g[start]
    
    for s in sg:
        visit = {s}
        stack = [s]
        
        while stack:
            u = stack.pop()
            if u not in g:
                ans[1] += 1 # 막대
                break
            if len(g[u]) == 2:
                ans[2] += 1 # 8자
                break
            for v in g[u]:
                if v in visit: continue
                visit.add(v)
                stack.append(v)
        else:
            ans[0] += 1 # 도넛
            
    answer = [start, *ans]
    return answer