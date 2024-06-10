from heapq import heappush, heappop

def solution(operations):
    minh = []
    maxh = []
    
    for operation in operations:
        oper, num = operation.split()
        num = int(num)
        
        if oper == 'I':
            heappush(minh, num)
            heappush(maxh, -num)
        else:
            if not minh: continue
            if num == 1:
                val = heappop(maxh)
                minh.remove(-val)
            else:
                val = heappop(minh)
                maxh.remove(-val)
    
    if not minh:
        return [0, 0]
    else:
        return [-maxh[0], minh[0]]