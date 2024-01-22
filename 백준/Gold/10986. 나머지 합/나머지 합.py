N, M = map(int, input().split())

arr = list(map(int, input().split()))
for i in range(1, N):
    arr[i] += arr[i-1]

acc = [0] * M
for val in arr:
    acc[val%M] += 1

ans = 0
for val in acc:
    ans += val * (val-1) / 2
ans += acc[0]

print(int(ans))