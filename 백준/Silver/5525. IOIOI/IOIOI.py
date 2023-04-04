N, M = int(input()), int(input())
arr = input()
tmp = 'I' + 'OI' * N
ans = 0

for i in range(0, M - 2 * N):
    for j in range(2 * N + 1):
        if arr[i+j] != tmp[j]:
            break
    else:
        ans += 1

print(ans)