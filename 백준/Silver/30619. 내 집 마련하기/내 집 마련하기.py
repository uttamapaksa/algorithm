N = int(input())
arr = [*map(int, input().split())]
ord = [0] * (N+1)
for i, v in enumerate(arr):
    ord[v] = i

M = int(input())
for _ in range(M):
    L, R = map(int, input().split())
    ord_2 = sorted(ord[L:R+1])
    for i in range(R-L+1):
        arr[ord_2[i]] = L+i
    print(*arr)
    for i in range(L, R+1):
        arr[ord[i]] = i