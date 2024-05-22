from  collections import deque

def solution(plans):
    tmp = []
    plans = deque(plans)
    while plans:
        sub, start, rest = plans.popleft()
        h, m = start.split(":")
        start = int(h) * 60 + int(m)
        tmp.append([sub, start, int(rest)])
    tmp.sort(key=lambda x: x[1])
    plans = deque(tmp)
    
    ans = []
    ready = []
    curr = plans[0][1]
    while plans:
        if ready and ready[-1][2] == 0:
            ans.append(ready.pop()[0])
        if curr == plans[0][1]:
            ready.append(plans.popleft())
            
        next = 10000
        if plans:
            next = plans[0][1] - curr
        if ready:
            next = min(ready[-1][2], next)
            ready[-1][2] -= next
        curr += next
        
    while ready:
        ans.append(ready.pop()[0])
        
    return ans