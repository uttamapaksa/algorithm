def solution(arr1, arr2):
    N = len(arr1)
    M = len(arr2[0])
    L = len(arr1[0])
    
    newArr = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            newArr[i][j] = sum(arr1[i][k] * arr2[k][j] for k in range(L))
            
    return newArr