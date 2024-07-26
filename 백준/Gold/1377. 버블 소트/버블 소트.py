N = int(input())
A = sorted((int(input()), i) for i in range(N))
ans = max(A[i][1] - i for i in range(N)) + 1
print(ans)