tc = 1
while 1:
    n = [*map(int, input())]
    if not n[0]: break

    while 1:
        if len(n) % 2:
            break
        for i in range(3, len(n), 2):
            if n[i] == n[i-2]:
                break
        nn = []
        for i in range(0, len(n), 2):
            nn += [n[i+1]] * n[i]
        if n == nn:
            break
        n = nn
        
    print(f'Test {tc}: {"".join(map(str, n))}')
    tc += 1