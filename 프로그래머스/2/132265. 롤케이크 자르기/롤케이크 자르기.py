def solution(arr):
    a = {}
    b = {}
    for v in arr:
        a[v] = a.get(v, 0) + 1
    
    ans = 0
    for v in arr:
        a[v] -= 1
        b[v] = b.get(v, 0) + 1
        if not a[v]:
            del a[v]
        
        if len(a) > len(b):
            continue
        elif len(a) == len(b):
            ans += 1
        else:
            break
        
    return ans