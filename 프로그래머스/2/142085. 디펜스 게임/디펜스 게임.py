from heapq import heappush, heappop

def solution(n, k, enemy):
    h = []
    for i in range(len(enemy)):
        e = enemy[i]
        heappush(h, -e)
        n -= e
        while h and k and n < 0:
            v = -heappop(h)
            n += v
            k -= 1
        if n < 0:
            break
            
    return i + int(n >= 0)