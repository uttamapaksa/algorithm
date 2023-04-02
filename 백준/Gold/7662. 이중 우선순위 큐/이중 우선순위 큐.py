import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def delete_maxh():
    while maxh and not visit[maxh[0][1]]:
        heappop(maxh)


def delete_minh():
    while minh and not visit[minh[0][1]]:
        heappop(minh)


for _ in range(int(input())):
    maxh = []
    minh = []
    visit = [0] * 1000001

    for i in range(int(input())):
        a, b = input().split()
        b = int(b)
        if a == 'I':
            heappush(minh, (b, i))
            heappush(maxh, (-b, i))
            visit[i] = 1

        elif b == 1:
            delete_maxh()
            if maxh:
                visit[maxh[0][1]] = 0
                heappop(maxh)
        else:
            delete_minh()
            if minh:
                visit[minh[0][1]] = 0
                heappop(minh)

    delete_maxh()
    delete_minh()
    if maxh or minh:
        print(-maxh[0][0], minh[0][0])
    else:
        print('EMPTY')