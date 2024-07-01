def solution(routes):
    routes.sort(key=lambda x: x[1])
    ans = 0
    last_camera = -30001
    
    for route in routes:
        if last_camera < route[0]:
            ans += 1
            last_camera = route[1]

    return ans
