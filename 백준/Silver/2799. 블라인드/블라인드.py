N, M = map(int, input().split())
arr = [[*input()] for _ in range(5*N+1)]
ans = [0, 0, 0, 0, 0]
for i in range(N):
    r = 5*i+1
    for j in range(M):
        c = 5*j+1
        curr = 0
        for k in range(r, r+4):
            if arr[k][c] == '*':
                curr += 1
            else:
                break
        ans[curr] += 1
print(*ans)