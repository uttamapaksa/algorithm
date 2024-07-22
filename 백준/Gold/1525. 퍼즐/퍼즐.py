from collections import deque


def sol():
    if first == last:
        return 0
    queue = deque([(first, first.index('0'))])
    visit = {first: 1}
    while queue:
        val, idx = queue.popleft()
        cnt = visit[val]
        val = list(val)
        for nidx in delta[idx]:
            val[idx], val[nidx] = val[nidx], val[idx]
            nval = ''.join(val)
            if nval == last:
                return cnt
            if nval not in visit:
                visit[nval] = cnt + 1
                queue.append((nval, nidx))
            val[idx], val[nidx] = val[nidx], val[idx]
    return -1


delta = [[1,3],[0,2,4],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[5,7]]
first = ''.join(''.join(input().split()) for _ in range(3))
last = '123456780'
print(sol())