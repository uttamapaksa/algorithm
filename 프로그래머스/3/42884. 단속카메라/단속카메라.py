def solution(routes):
    routes.sort(key=lambda x: (-x[1], x[0]))
    ans = 0
    
    while routes:
        s, e = routes.pop()
        ans += 1
        while routes and routes[-1][0] <= e:
            routes.pop()
        
    return ans
