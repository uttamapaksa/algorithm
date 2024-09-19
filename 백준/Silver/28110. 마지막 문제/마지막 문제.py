N = int(input())
A = sorted(map(int, input().split()))

ans, diff = -1, 0
if A[N-1] - A[0] > N-1:
    for i in range(N-1):
        tmp = (A[i+1] - A[i]) >> 1
        if diff < tmp:
            diff = tmp
            ans = A[i] + tmp
            
print(ans)