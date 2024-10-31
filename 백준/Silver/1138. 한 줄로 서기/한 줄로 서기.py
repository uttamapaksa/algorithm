N = int(input())
ans = [0] * N
for person, order in enumerate(map(int, input().split())):
    tmp = -1
    for i in range(N):
        if not ans[i]:
            tmp += 1
            if tmp == order:
                ans[i] = person+1
                break
print(*ans)