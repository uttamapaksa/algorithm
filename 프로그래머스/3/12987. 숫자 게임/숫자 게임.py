def solution(A, B):
    A.sort()
    B.sort()
    N = len(A)
    
    ans = 0
    i = j = 0
    while i < N and j < N:
        a, b = A[i], B[j]
        if a < b:
            i += 1
            ans += 1
        j += 1
            
    return ans    
