from collections import deque

def solution(relation):
    answer = 0
    N = len(relation)
    M = len(relation[0])
    Q = deque([(0, set())])
    keys = []
    
    while Q:
        k, visit = Q.popleft()
        for key in keys:
            if key.issubset(visit):
                break
        else:
            tups = set()
            for row in relation:
                tup = tuple(row[c] for c in visit)
                tups.add(tup)

            if len(tups) == N:
                keys.append(visit)
                continue

            for i in range(k, M):
                if i in visit: continue
                Q.append((i+1, visit | {i}))
            
    return len(keys)
