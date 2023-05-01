def Queen(r):
    global ans
    if r == N:
        ans += 1
        return
    for c in range(N):
        if col[c]: continue  # 세로 겹치면
        rd = r + c
        ld = r - c
        if rd in rdia or ld in ldia: continue  # 대각선 겹치면
        col[c] = 1
        ldia.add(ld)
        rdia.add(rd)
        Queen(r+1)
        col[c] = 0  # 백트래킹
        ldia.remove(ld)
        rdia.remove(rd)


N = int(input())
col = [0] * N  # 세로 목록
rdia = set()  # 우상향 대각선 목록
ldia = set()  # 좌상향 대각선 목록
ans = 0
Queen(0)
print(ans)