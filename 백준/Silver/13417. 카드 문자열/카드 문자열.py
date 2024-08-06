from collections import deque

for _ in range(int(input())):
    n = input()
    ans = deque()
    for  v in input().split():
        if not ans: ans.append(v)
        elif v > ans[0]: ans.append(v)
        else: ans.appendleft(v)
    print(''.join(ans))