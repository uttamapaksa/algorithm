def solution(elements):
    N = len(elements)
    elements = elements + elements
    sums = set()
    
    for i in range(1, N+1):
        init = sum(elements[:i])
        sums.add(init)
        for j in range(N-1):
            init += elements[i+j]
            init -= elements[j]
            sums.add(init)
    
    answer = len(sums)
    return answer