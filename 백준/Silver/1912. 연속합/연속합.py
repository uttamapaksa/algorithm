n = int(input())
arr = list(map(int, input().split()))

for i in range(n-2, -1, -1):
    arr[i] = max(arr[i], arr[i] + arr[i+1])

print(max(arr))