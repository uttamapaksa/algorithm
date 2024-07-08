def sol():
    cnt = 0
    for i in range(2, N+1):
        for j in range(1, N//i + 1):
            if i*j in nums:
                nums.remove(i*j)
                cnt += 1
                if cnt == K:
                    return i*j


N, K = map(int, input().split())
nums = set(range(2, N+1))
print(sol())