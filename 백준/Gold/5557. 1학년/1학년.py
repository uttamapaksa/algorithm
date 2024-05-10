_ = input()
arr = [*map(int, input().split())]
first = arr.pop(0)
res = arr.pop()

prev = {first: 1}
for e in arr:
    curr = {}
    for k, cnt in prev.items():
        if 0 <= k+e <= 20:
            curr[k+e] = curr.get(k+e, 0) + cnt
        if 0 <= k-e <= 20:
            curr[k-e] = curr.get(k-e, 0) + cnt
    prev = curr

print(prev.get(res, 0))