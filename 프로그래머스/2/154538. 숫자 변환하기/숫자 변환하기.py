from collections import deque

def solution(x, y, n):
    V = [-1] * (y+1)    
    Q = deque([(x)])
    V[x] = 0
    
    while Q:
        u = Q.popleft()
        for v in (u+n, u*2, u*3):
            if v > y or V[v] != -1: continue
            Q.append(v)
            V[v] = V[u] + 1
    
    return V[y]