blanks = [
    {4, 7, 10},
    {0, 1, 3, 4, 6, 7, 9, 10, 12, 13},
    {3, 4, 10, 11},
    {3, 4, 9, 10},
    {1, 4, 9, 10, 12, 13},
    {4, 5, 9, 10},
    {4, 5, 10},
    {3, 4, 6, 7, 9, 10, 12, 13},
    {4, 10},
    {4, 9, 10}
]

arr = [[*input()] for _ in range(5)]
res = []
for c in (0, 4, 8, 12):
    curr = set()    
    for i in range(5):
        for j in range(3):
            if arr[i][c+j] == '#':
                curr.add(i*3+j)
    for i in range(10):
        if not (blanks[i] & curr):
            res.append(i)
            break

print(f'{res[0]}{res[1]}:{res[2]}{res[3]}')