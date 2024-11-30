from collections import deque

prev = deque()
curr = -1
post = deque()
cache = 0
N, Q, C = map(int, input().split())
pages = [0] + list(map(int, input().split()))

for _ in range(Q):
    ipt = input().split()
    if ipt[0] == "B":
        if prev:
            post.appendleft(curr)
            curr = prev.pop()
    elif ipt[0] == 'F':
        if post:
            prev.append(curr)
            curr = post.popleft()
    elif ipt[0] == 'A':
        while post:
            cache -= pages[post.pop()]
        if curr != -1:
            prev.append(curr)
        curr = int(ipt[1])
        cache += pages[curr]
        while cache > C:
            cache -= pages[prev.popleft()]
    else:
        if len(prev) < 2: continue
        tmp = deque()
        tmp.appendleft(prev.pop())
        while prev:
            if tmp[0] == prev[-1]:
                cache -= pages[prev.pop()]
            else:
                tmp.appendleft(prev.pop())
        prev = tmp


print(curr)
prev.reverse()
print(*prev if prev else [-1])
print(*post if post else [-1])
