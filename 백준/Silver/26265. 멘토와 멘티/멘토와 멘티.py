d = {}
for _ in range(int(input())):
    a, b = (input().split())
    d.setdefault(a, []).append(b)
print('\n'.join(f'{k} {v}' for k in sorted(d.keys()) for v in sorted(d[k], reverse=1)))