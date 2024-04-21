def solution(cap, n, deliveries, pickups):
    answer = 0
    deliverie = []
    pickup = []
    for i in range(n):
        if deliveries[i]:
            deliverie.append([deliveries[i], i+1])
        if pickups[i]:
            pickup.append([pickups[i], i+1])
    
    def 배달():
        rest = cap
        last = 0
        while rest and deliverie:
            val, idx = deliverie[-1]
            if not last:
                last = idx
            if rest >= val:
                rest -= val
                deliverie.pop()
            else:
                deliverie[-1][0] -= rest
                rest = 0
                
        return last
    
    def 수거():
        rest = cap
        last = 0
        while rest and pickup:
            val, idx = pickup[-1]
            if not last:
                last = idx
            if rest >= val:
                rest -= val
                pickup.pop()
            else:
                pickup[-1][0] -= rest
                rest = 0
                
        return last
    
    while True:
        d = 배달()
        p = 수거()
        m = max(d, p)
        if not m:
            break
        answer += 2 * m 
    
    return answer