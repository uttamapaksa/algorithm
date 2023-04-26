K = int(input())

a = []
for i in range(K):
    a.append(list(map(int, input().split())))

for i in a:
    cnt = 0
    for j in a:
        if j[0] > i[0] and j[1] > i[1]:
            cnt += 1
    print(cnt + 1, end=' ')