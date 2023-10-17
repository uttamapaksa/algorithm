N, M = tuple(map(int, (input().split())))

trees = list(map(int, input().split()))

start = 0
end = 2000000000
result = 0

while start <= end:
    take = 0

    H = (start+end) // 2
    
    for i in trees:
        if H < i:
            take += i - H

    if take < M: # 만족 안 될 경우
        end = H-1
    else:        # 만족 될 경우
        start = H+1
        result = H

print(result)
        