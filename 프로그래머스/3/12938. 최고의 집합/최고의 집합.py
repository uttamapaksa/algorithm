def solution(n, s):
    m = s // n
    d = s % n
    arr = [m+1] * d + [m] * (n-d)
    arr.sort()
    
    if not arr[0]:
        return [-1]
    return arr
    