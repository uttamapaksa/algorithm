from heapq import heapify, heappush, heappop

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
                minh.remove(-heappop(maxh))
                heapify(minh)
            else:
                maxh.remove(-heappop(minh))
                heapify(maxh)
    
    if not minh:
        return [0, 0]
    else:
        return [-maxh[0], minh[0]]