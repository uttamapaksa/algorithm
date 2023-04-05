from collections import deque

for _ in range(int(input())):
    F = input()
    n = int(input())
    if not n: junk = input(); arr = deque([])
    else: arr = deque(input()[1:-1].split(','))

    error = r = 0
    for order in F:
        if order == 'R': r ^= 1
        else:
            if not len(arr): error = 1; break
            elif r: arr.pop()
            else: arr.popleft()

    if error:
        print('error')
    else:
        print('[', end='')
        if r:
            for i in range(len(arr)-1, 0, -1):
                print(arr[i], end='')
                print(',', end='')
            if len(arr) > 0:
                print(arr[0], end='')
        else:
            for i in range(0, len(arr)-1):
                print(arr[i], end='')
                print(',', end='')
            if len(arr) > 0:
                print(arr[-1], end='')
        print(']')
