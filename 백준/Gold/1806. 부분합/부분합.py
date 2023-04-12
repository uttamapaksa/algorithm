import sys; input = sys.stdin.readline

N, S = map(int, input().split())
arr = [*map(int, input().split())]

ans = 100001
tmp = 0
cnt = 0
for i in range(N):
    cnt += 1
    if cnt == ans:
        tmp -= arr[i-cnt+1]
        cnt -= 1
    tmp += arr[i]
    if tmp >= S:
        ans = min(ans, cnt)
        for j in range(cnt-1, 0, -1):
            if tmp - arr[i-j] >= S:
                tmp -= arr[i-j]
                cnt -= 1
                ans = (min(ans, cnt))
            else:
                break

print(ans % 100001)