ans = []
while True:
    try:
        n = int(input())
        a = '-'
        for _ in range(n):
            a = a + ' ' * len(a) + a
        ans.append(a)
    except:
        print('\n'.join(ans))
        break