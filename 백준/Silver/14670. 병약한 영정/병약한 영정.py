medi = {}
mediset = set()
for _ in range(int(input())):
    e, n = map(int, input().split())
    medi[e] = n
    mediset.add(e)

for _ in range(int(input())):
    _, *es = map(int, input().split())
    if not set(es).issubset(mediset):
        print('YOU DIED')
    else:
        print(' '.join(map(str, (medi[e] for e in es))))
