for _ in range(int(input())):
    N, M = map(int, input().split())
    A, B = [*map(int, input().split())], [*map(int, input().split())]
    A.sort(); B.sort()
    
    ans, j = N, M-1
    for i in range(N-1, -1, -1):
        while A[i] <= B[j] and j > -1:
            j -= 1
        ans += j
    print(ans)