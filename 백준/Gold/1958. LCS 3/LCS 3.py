a = input(); b = input(); c = input()
n, m, l = len(a), len(b), len(c)
prev = [[0] * (l+1) for _ in range(m+1)]
curr = [[0] * (l+1) for _ in range(m+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(1, l+1):
            if a[i-1] == b[j-1] == c[k-1]:
                curr[j][k] = prev[j-1][k-1] + 1
            else:
                curr[j][k] = max(prev[j][k], curr[j-1][k], curr[j][k-1])
    prev, curr = curr, prev

print(prev[m][l])
