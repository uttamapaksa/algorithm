index = ['null', 'null', 'null', 'null']  # up, down, right, left

n = int(input())
for _ in range(n):
    x, y, d = input().split()
    if d == 'U':
        if index[0] == 'null':
            index[0] = int(y)
        else:
            index[0] = max(index[0], int(y))
    elif d == 'D':
        if index[1] == 'null':
            index[1] = int(y)
        else:
            index[1] = min(index[1], int(y))
    elif d == 'R':
        if index[2] == 'null':
            index[2] = int(x)
        else:
            index[2] = max(index[2], int(x))
    else:
        if index[3] == 'null':
            index[3] = int(x)
        else:
            index[3] = min(index[3], int(x))

if 'null' in index:
    print('Infinity')
else:
    print((index[1]-index[0]-1) * (index[3]-index[2]-1))