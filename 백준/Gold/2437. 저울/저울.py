_ = input()
nums = sorted(map(int, input().split()))
done = 0

for num in nums:
    if num-1 > done:
        break
    done += num

print(done+1)