def solution(n):
    if n & 1: return 0
    
    p, c = 1, 3
    for _ in range((n >> 1) - 1):
        p, c = (p + c) % 1000000007, (p * 2 + c * 3) % 1000000007
        
    return c