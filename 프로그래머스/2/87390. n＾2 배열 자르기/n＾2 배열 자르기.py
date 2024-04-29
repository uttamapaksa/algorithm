def solution(n, left, right):
    
    def row(k, l=0, r=n):
        return ([k] * k + list(range(k + 1, n + 1)))[l:r]
    
    answer = []
    l1, l2 = left // n + 1, left % n
    r1, r2 = right // n + 1, right % n
    
    if l1 == r1:
        answer = row(l1, l2, r2 + 1)
    else:
        answer += row(l1, l2)
        for i in range(l1 + 1, r1):
            answer += row(i)
        answer += row(r1, 0, r2 + 1)
    
    return answer

