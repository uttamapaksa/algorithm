def solution(n, stations, w):
    area = w * 2 + 1
    start = 1
    ans = 0
    
    for station in stations:
        if station - w - start > 0:
            ans += (station - w - start - 1) // area + 1 
        start = station + w + 1
    if n + 1 - start > 0:
        ans += (n - start) // area + 1
    
    return ans