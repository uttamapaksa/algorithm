def BnW(r, c, n):
    fst = arr[r][c]
    snd = trd = fth = ''
    for i in range(r, r + n):
        for j in range(c, c + n):
            if arr[i][j] != fst:
                nn = n//2
                fst = BnW(r, c, nn)
                snd = BnW(r, c+nn, nn)
                trd = BnW(r+nn, c, nn)
                fth = BnW(r+nn, c+nn, nn)
                return f'({fst}{snd}{trd}{fth})'
    return fst

N = int(input())
arr = [[*input()] for _ in range(N)]
print(BnW(0, 0, N))