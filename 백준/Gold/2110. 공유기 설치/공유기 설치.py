import sys; input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

first = arr[0]  # 시작점
minv = arr[1] - first
pre = arr[1]
for i in range(2, N):
    cur = arr[i]
    minv = min(minv, cur - pre)
    pre = cur
start = minv  # 최소간격
end = arr[N-1] - first  # 최대간격
ans = 1  # 정답간격

while start <= end:
    mid = (start + end) // 2
    now = first
    cnt = 1

    for i in range(1, N):
        if arr[i] >= now + mid:
            now = arr[i]
            cnt += 1
            if cnt > C: break
    
    if cnt >= C:
        start = mid + 1   
        ans = mid
    else: 
        end = mid - 1

print(ans)