N, M = int(input()), int(input())
l = len(str(N))

# button 리스트 생성
if M: broken = input().split()
else: broken = []
button = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in broken: button.remove(i)

# dp 최댓값 설정
if M == 10 or button == ['0']: maxv = N
else:
    if '0' in button:
        if N < int(button[-1] * l): maxv = int(button[-1] * l)
        else: maxv = int(button[1] + '0' * l)
    else:
        if N < int(button[-1] * l): maxv = int(button[-1] * l)
        else: maxv = int(button[0] * (l + 1))

# dp 생성
dp = {i: 100 - i for i in range(101)}
if maxv >= 100:
    for i in range(101, maxv + 2):
        dp[i] = i - 100

# dp 적용
# bottom - top
for i in range(0, maxv + 1):
    for j in str(i):
        if j not in button: break  # 버튼만으로 접근 불가능
    else:  # 버튼만으로 접근 불가능
        dp[i] = min(dp[i], len(str(i)))
    if i: dp[i] = min(dp[i], dp[i-1] + 1, dp[i+1] + 1)
    else: dp[i] = min(dp[i], dp[i+1] + 1)
# top - down
for i in range(maxv, -1, -1):
    for j in str(i):
        if j not in button: break  # 버튼만으로 접근 불가능
    else:  # 버튼만으로 접근 불가능
        dp[i] = min(dp[i], len(str(i)))
    if i: dp[i] = min(dp[i], dp[i-1] + 1, dp[i+1] + 1)
    else: dp[i] = min(dp[i], dp[i+1] + 1)
# dp[N] 출력
print(dp[N])