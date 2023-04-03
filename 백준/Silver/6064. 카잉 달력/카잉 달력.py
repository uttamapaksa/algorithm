for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    a, b = M, N

    while b:
        c = a % b
        a, b = b, c
    maxs = M * N // a

    ans = set()
    for i in range(x, maxs + 1, M):
        ans.add(i)
    for i in range(y, maxs + 1, N):
        if i in ans:
            print(i)
            break
    else:
        print(-1)