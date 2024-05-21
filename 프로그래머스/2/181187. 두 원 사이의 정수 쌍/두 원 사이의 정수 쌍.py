from math import ceil

def solution(r1, r2):
    dot1 = r1
    for w in range(1, r1+1):
        h1 = (r1**2 - w**2) ** (1/2) 
        dot1 += ceil(h1) - 1
        
    dot2 = r2
    for w in range(1, r2+1):
        h2 = (r2**2 - w**2) ** (1/2) 
        dot2 += int(h2)
    
    return (dot2 - dot1) * 4