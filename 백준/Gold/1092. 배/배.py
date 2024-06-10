n = int(input())
ship = [*map(int, input().split())]
m = int(input())
box = [*map(int, input().split())]
ship.sort()
box.sort()

if box[-1] > ship[-1]:
    print(-1)
else:
    # dp
    dp = [0] * n
    i = 0
    for v in box:
        if ship[i] >= v:
            dp[i] += 1
        else:
            while True:
                i += 1
                if ship[i] >= v:
                    dp[i] += 1
                    break
    # flatten
    updated = 1
    while updated:
        updated = 0
        for i in range(n-1):
            if dp[i] > dp[i+1]:
                sumv = dp[i] + dp[i+1]
                half = sumv // 2
                dp[i] = half
                dp[i+1] = sumv - half
                updated = 1
    print(max(dp))