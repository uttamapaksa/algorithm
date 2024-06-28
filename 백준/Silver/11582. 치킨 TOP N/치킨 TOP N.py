n = int(input())
arr = list(map(int, input().split()))
m = int(input())
l = n // m

ans = []
for i in range(m):
    ans.extend(sorted(arr[l*i:l*(i+1)]))
print(*ans)