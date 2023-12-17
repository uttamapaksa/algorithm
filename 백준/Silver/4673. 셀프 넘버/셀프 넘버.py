nums = {i: 0 for i in range(1, 10001)}
for i in range(1, 10000):
    tmp = i
    for j in str(i):
        tmp += int(j)
    nums[tmp] = 1

for i in range(1, 10001):
    if not nums[i]:
        print(i)