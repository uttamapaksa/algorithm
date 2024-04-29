def solution(k, tangerine):
    
    tangerines = {}
    for t in tangerine:
        if t in tangerines:
            tangerines[t] += 1
        else:
            tangerines[t] = 1
    tangerines = sorted(tangerines.items(), key=lambda x: -x[1])
    
    answer = 0
    for _, v in tangerines:
        answer += 1
        k -= v
        if k <= 0:
            break
        
    return answer