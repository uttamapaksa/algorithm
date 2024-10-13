N = int(input())
mines = tuple(int(input()) for _ in range(N))
orders = sorted(enumerate(mines), key=lambda x: x[1])
visit = [0] * N
ans = []

for i in range(N-1, -1, -1):
    order = orders[i][0]
    if visit[order]: continue
    visit[order] = 1
    ans.append(order+1)
    for j in range(order, N-1):
        if mines[j] > mines[j+1]:
            visit[j+1] = 1
        else:
            break
    for j in range(order, 0, -1):
        if mines[j] > mines[j-1]:
            visit[j-1] = 1
        else:
            break

print('\n'.join(map(str, sorted(ans))))