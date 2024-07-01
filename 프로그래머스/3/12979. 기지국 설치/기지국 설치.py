def solution(n, stations, w):
    stations = [(station - w, station + w) for station in stations]
    area = []
    s, e = 0, 0
    for station in stations:
        if e >= station[0]-1:
            e = station[1]
        else:
            area.append((s, e))
            s, e = station
    area.append((s, e))
    area.append((n+1, n+1))
    
    ans = 0
    div = 2*w+1
    for i in range(len(area)-1):
        diff = area[i+1][0] - area[i][1] - 1
        ans += (diff-1) // div + 1
    
    return ans