from collections import deque


def bfs():
    visit = {p: 0 for p in ps}
    a, b = map(int, input().split())
    visit[a] = 1
    queue = deque([(a, 0)])
    while queue:
        curr, cnt = queue.popleft()
        if curr == b:
            return str(cnt)
        # 1000
        tmp = curr%1000
        for i in range(1, 10):
            next = i*1000 + tmp
            if next in visit and not visit[next]:
                visit[next] = 1
                queue.append((next, cnt+1))
        # 100
        tmp = (curr//1000)*1000 + curr%100
        for i in range(10):
            next = i*100 + tmp
            if next in visit and not visit[next]:
                visit[next] = 1
                queue.append((next, cnt+1))
        # 10
        tmp = (curr//100)*100 + curr%10
        for i in range(10):
            next = i*10 + tmp
            if next in visit and not visit[next]:
                visit[next] = 1
                queue.append((next, cnt+1))
        # 1
        tmp = (curr//10)*10
        for i in range(10):
            next = i + tmp
            if next in visit and not visit[next]:
                visit[next] = 1
                queue.append((next, cnt+1))
    return "Impossible"


ps = set(range(1000, 10000))
for i in range(2, 101):
    for j in range(i*i, 10001, i):
        ps.discard(j)


ans = []
tc = int(input())
for _ in range(tc):
    ans.append(bfs())
print("\n".join(ans))