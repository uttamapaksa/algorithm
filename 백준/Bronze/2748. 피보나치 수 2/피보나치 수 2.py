dp = [0, 1]
for i in range(2, int(input())+1):
    dp.append(dp[-1] + dp[-2])
print(dp[-1])