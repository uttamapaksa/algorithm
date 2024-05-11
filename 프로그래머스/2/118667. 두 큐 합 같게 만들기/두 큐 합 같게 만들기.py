def solution(q1, q2):
    curr = sum(q1)
    q1 += q2
    sums = sum(q1) // 2
    
    n = len(q1)
    i = 0
    j = n // 2 - 1
    ans = 0
    
    while curr != sums:
        ans += 1
        if curr > sums:
            curr -= q1[i]
            i += 1
        else:
            j += 1
            if j == n:
                 break
            curr += q1[j]
    
    return ans if curr == sums else -1