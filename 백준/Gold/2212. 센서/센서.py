N, K = int(input()), int(input())
arr = sorted([*map(int, input().split())])
diff = sorted([(arr[i+1]-arr[i], i+1) for i in range(N-1)], reverse=True) 
diff = [0] + sorted([diff[i][1] for i in range(min(N-1, K-1))]) + [N]
ans = sum(arr[diff[i+1]-1] - arr[diff[i]] for i in range(len(diff)-1))
print(ans)