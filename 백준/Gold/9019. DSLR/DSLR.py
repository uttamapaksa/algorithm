from collections import deque


def D(x):
    return (2 * x) % 10000


def S(x):
    if not n: return 9999
    return x - 1


def L(x):
    tmp = 0
    tmp += x // 1000
    x %= 1000
    tmp += (x // 100) * 1000
    x %= 100
    tmp += (x // 10) * 100
    x %= 10
    tmp += x * 10
    return tmp

def R(x):
    tmp = 0
    tmp += (x // 1000) * 100
    x %= 1000
    tmp += (x // 100) * 10
    x %= 100
    tmp += (x // 10)
    x %= 10
    tmp += x * 1000
    return tmp


for _ in range(int(input())):
    A, B = map(int, input().split())
    visit = {i: 0 for i in range(0, 10000)}
    visit[A] = 1
    q = deque([(A, '')])
    while q:
        n, order = q.popleft()
        dd, ss, ll, rr = D(n), S(n), L(n), R(n)
        if dd == B: print(order + 'D'); break
        else:
            if not visit[dd]:
                visit[dd] = 1
                q.append((dd, order + 'D'))
        if ss == B: print(order + 'S'); break
        else:
            if not visit[ss]:
                visit[ss] = 1
                q.append((ss, order + 'S'))
        if ll == B: print(order + 'L'); break
        else:
            if not visit[ll]:
                visit[ll] = 1
                q.append((ll, order + 'L'))
        if rr == B: print(order + 'R'); break
        else:
            if not visit[rr]:
                visit[rr] = 1
                q.append((rr, order + 'R'))