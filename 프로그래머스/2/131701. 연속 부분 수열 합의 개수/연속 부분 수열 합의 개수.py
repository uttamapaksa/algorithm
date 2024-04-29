def solution(elements):
    N = len(elements)
    sumv = sum(elements)
    sums = {sumv}
    
    elements = elements + elements
    
    for i in range(1, N//2 + 2):
        init = sum(elements[:i])
        sums.add(init)
        sums.add(sumv - init)
        for j in range(N-1):
            init += elements[i+j]
            init -= elements[j]
            sums.add(init)
            sums.add(sumv - init)
    
    answer = len(sums)
    return answer