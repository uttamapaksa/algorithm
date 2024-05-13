from collections import deque

def solution(n):
    INF = 100000000
    visit = {n: 0}
    queue = deque([n])
    while queue:
        u = queue.popleft()
        if not u: break
        for i in range(1, 9):
            if not u % (10 ** i): continue
            v = u + 10 ** (i-1)
            if not v: return  visit[u] + 1
            if 0 < v <= INF and v not in visit:
                visit[v] = visit[u] + 1
                queue.append(v)
            v = u - 10 ** (i-1)
            if not v: return  visit[u] + 1
            if 0 <= v <= INF and v not in visit:
                visit[v] = visit[u] + 1
                queue.append(v)
            break
        else:
            return visit[u] + 1
            
    return visit[0]