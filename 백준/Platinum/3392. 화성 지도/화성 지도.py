def update(node, start, end):
    # cover update
    if y2 < start or end < y1:
        return
    if y1 <= start and end <= y2:
        cover[node] += val
    else:
        mid = (start + end) // 2
        update(node*2, start, mid)
        update(node*2+1, mid+1, end)
    # tree update
    if cover[node]:
        tree[node] = end - start + 1
    else:
        tree[node] = tree[node*2] + tree[node*2+1]


MAX_LENGTH = 30000
event = []
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    event.append((x1, y1, y2-1, 1)) # start
    event.append((x2, y1, y2-1, -1)) # end
event.sort()

tree = [0]*2*MAX_LENGTH*4 
cover = [0]*2*MAX_LENGTH*4

ans = 0
prev = event[0][0]
for x, y1, y2, val in event:
    ans += tree[1] * (x - prev)
    prev = x
    update(1, 0, MAX_LENGTH)

print(ans)