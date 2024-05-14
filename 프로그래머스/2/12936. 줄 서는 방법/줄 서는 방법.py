def solution(n, k):
    arr = list(range(1, n+1))
    k -= 1
    div = 1
    for i in range(2, n):
        div *= i
    
    ans = []
    for i in range(n-1, 0, -1):
        idx = k // div
        k %= div
        div //= i
        ans.append(arr.pop(idx))
    ans.append(arr.pop())
    
    return ans