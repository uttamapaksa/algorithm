K, N = map(int, input().split())
if (N == 1): print(-1)
else: print(int((K*N-1)//(N-1))+1)