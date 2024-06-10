from heapq import heappush, heappop

def solution(operations):
    n = len(operations)
    deleted = [0] * n
    minh = []
    maxh = []
    
    for i in range(n):
        oper, num = operations[i].split()
        num = int(num)
        
        if oper == 'I':
            heappush(minh, (num, i))
            heappush(maxh, (-num, i))
        elif num == 1:
            while maxh and deleted[maxh[0][1]]:
                heappop(maxh)
            if maxh:
                deleted[heappop(maxh)[1]] = 1
        else:
            while minh and deleted[minh[0][1]]:
                heappop(minh)
            if minh:
                deleted[heappop(minh)[1]] = 1
                
    while maxh and deleted[maxh[0][1]]:
        heappop(maxh)
    while minh and deleted[minh[0][1]]:
        heappop(minh)
    
    if not minh:
        return [0, 0]
    else:
        return [-maxh[0][0], minh[0][0]]