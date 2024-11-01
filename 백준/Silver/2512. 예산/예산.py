from math import ceil

N = int(input())
arr = list(map(int, input().split())) + [0]
arr.sort(reverse=True)
M = int(input())

sums = sum(arr)
for i in range(1, N+1):
    if sums <= M:
        break
    diff = arr[i-1] - arr[i]
    if diff * i >= sums - M:
        arr[0] -= ceil((sums - M) / i)
        break
    sums -= diff * i
    arr[0] -= diff

print(arr[0])