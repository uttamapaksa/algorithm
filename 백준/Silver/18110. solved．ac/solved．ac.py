N = int(input())
arr = sorted([int(input()) for _ in range(N)])
if not N:
    print(0)
else:
    M = N * 15 / 100
    if M % 1 >= 0.5:
        M = int(M + 1)
    else:
        M = int(M)
    arr = arr[M:N-M]

    ans = sum(arr) / len(arr)
    if ans % 1 >= 0.5:
        ans = int(ans + 1)
    else:
        ans = int(ans)
    print(ans)