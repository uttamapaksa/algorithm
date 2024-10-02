for _ in range(int(input())):
    N, M = map(int, input().split())
    A, B = [*map(int, input().split())], [*map(int, input().split())]
    A.sort(); B.sort()
    
    ans = j = 0
    for i in range(N):
        while j < M and A[i] > B[j]:
            j += 1
        ans += j
    print(ans)