from math import gcd

def intA(A, B):
    g = A[0]
    for i in range(1, len(A)):
        g = gcd(g, A[i])
        if g == 1:
            return 0
    for v in B:
        if v % g == 0:
            return 0
    return g

def solution(arrA, arrB):
    answer = max(intA(arrA, arrB), intA(arrB, arrA))    
    return answer