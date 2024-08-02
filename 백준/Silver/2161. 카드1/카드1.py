a = list(range(1, int(input())+1))
r = []

while len(a) > 1:
    r.append(a.pop(0))
    a.append(a.pop(0))
r.append(a.pop(0))

print(*r)