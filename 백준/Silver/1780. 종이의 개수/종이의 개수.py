def d9(r, c, n):
    k = arr[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if arr[i][j] != k:
                nn = n//3
                d9(r, c, nn)
                d9(r, c+nn, nn)
                d9(r, c+nn+nn, nn)
                d9(r+nn, c, nn)
                d9(r+nn, c+nn, nn)
                d9(r+nn, c+nn+nn, nn)
                d9(r+nn+nn, c, nn)
                d9(r+nn+nn, c+nn, nn)
                d9(r+nn+nn, c+nn+nn, nn)
                return 
    global ans; ans[k] += 1

N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
ans = [0, 0, 0]
d9(0, 0, N)
for i in(-1, 0, 1):
    print(ans[i])