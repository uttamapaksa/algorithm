def solution(k, d):
    ans = 0
    ans += 1 + (d//k)*2
    
    for w in range(k, d+1, k):
        h = (d**2 - w**2) ** (1/2)
        ans += h//k
    
    return ans