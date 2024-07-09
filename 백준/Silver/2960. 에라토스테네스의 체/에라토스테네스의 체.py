def sol():
    cnt = 0
    for i in range(2, N+1):
        for j in range(i, N+1, i):
            if j in nums:
                nums.remove(j)
                cnt += 1
                if cnt == K:
                    return j


N, K = map(int, input().split())
nums = set(range(2, N+1))
print(sol())