from collections import deque

def goto_destination(cl, sr, sc, er, ec):
    global G, client
    queue = deque([(sr, sc, 1)])
    visit = {sr*100+sc}
    while queue:
        r, c, d = queue.popleft()
        for nr, nc in ((r-1,c), (r,c-1), (r,c+1), (r+1,c)):
            if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] == 1 or (nr*100+nc) in visit: continue
            visit.add(nr*100+nc)
            if nr == er and nc == ec:
                G += d
                del client[cl]
                return 1
            if G <= d: continue
            queue.append((nr, nc, d+1))
    return 0

def shortest_client(r, c):
    global G
    if arr[r][c] > 1:
        cl = arr[r][c]
        arr[r][c] = 0
        return cl
    curr = deque([(r, c, 1)])
    client = []
    visit = {r*100+c}
    while curr:
        next = deque()
        while curr:
            r, c, d = curr.popleft()
            for nr, nc in ((r-1,c), (r,c-1), (r,c+1), (r+1,c)):
                if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] == 1 or (nr*100+nc) in visit: continue
                visit.add(nr*100+nc)
                if arr[nr][nc] > 1:
                    client.append((nr, nc, arr[nr][nc]))
                if G <= d: continue
                next.append((nr, nc, d+1))
        if client:
            client.sort(reverse=True)
            nr, nc, cl = client.pop()
            arr[nr][nc] = 0
            G -= d
            return cl
        curr = next
    return -1

N, M, G = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
R, C = map(int, input().split())
R-=1; C-=1

client = {}
for i in range(2, M+2):  # 0은 빈칸, 1은 벽, 2~는 손님
    sr, sc, er, ec = map(int, input().split())
    sr-=1; sc-=1; er-=1; ec-=1
    client[i] = (sr, sc, er, ec)
    arr[sr][sc] = i

r, c = R, C
while client:
    cl = shortest_client(r, c)
    if cl == -1:
        print(-1)
        break
    sr, sc, er, ec = client[cl]
    if not goto_destination(cl, sr, sc, er, ec):
        print(-1)
        break
    r, c = er, ec
else:
    print(G)