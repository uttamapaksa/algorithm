def solution(arr):
    N = len(arr)
    ans = [-1] * N
    
    S = []
    for i in range(N):
        while S and arr[S[-1]] < arr[i]:
            ans[S.pop()] = arr[i]
        S.append(i)
        
    return ans