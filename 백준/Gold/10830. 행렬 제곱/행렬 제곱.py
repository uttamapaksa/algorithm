def matrix_power(mat, pow, mod):
    if pow == 1:
        return [[col % mod for col in row] for row in mat]
    
    half = matrix_power(mat, pow // 2, mod)
    ret = [[sum(half[i][k] * half[k][j] for k in range(N)) % mod for j in range(N)] for i in range(N)]
    if pow % 2 == 1:
        ret = [[sum(ret[i][k] * mat[k][j] for k in range(N)) % mod for j in range(N)] for i in range(N)]

    return ret


N, B = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
ret = matrix_power(mat, B, 1000)
for row in ret:
    print(*row)