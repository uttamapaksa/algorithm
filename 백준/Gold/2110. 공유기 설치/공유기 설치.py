import sys; input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
first = arr[0]
start = 1
end = arr[N-1]
ans = 1

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