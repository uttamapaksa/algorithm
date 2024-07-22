from collections import deque


def sol(s, i):
    if s == e:
        return 0
    queue = deque([(s, i)])
    memo = {s: 1}
    while queue:
        v, i = queue.popleft()
        for ni in delta[i]:
            pv = v % ten[ni+1] - v % ten[ni]
            nv = pv // ten[ni] * ten[i]
            nv = v - pv + nv
            if nv == e:
                return memo[v]
            if nv not in memo:
                memo[nv] = memo[v] + 1
                queue.append((nv, ni))
    return -1


delta = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]
ten = [10 ** i for i in range(10)]
s = ''.join(''.join(input().split()) for _ in range(3))
e = 123456780
print(sol(int(s), 8 - s.index('0')))