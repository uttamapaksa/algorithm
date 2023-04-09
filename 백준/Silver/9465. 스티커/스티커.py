import sys
input = sys.stdin.readline
for _ in range(int(input())):
    
    n = int(input())
    arr = [[*map(int, input().split())] for _ in range(2)]
    dp = [0] * n
    dp[0] = (arr[0][0], arr[1][0], 0)
    
    for i in range(1, n):
        A, B, C = dp[i-1]
        dp[i] = (max(B, C) + arr[0][i], max(A, C) + arr[1][i], max(A, B))
        
    print(max(dp[-1]))