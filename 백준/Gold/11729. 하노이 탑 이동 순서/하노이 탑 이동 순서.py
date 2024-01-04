N = int(input())
p = {1: 1, 2: 3, 3: 2}
n = {1: 2, 2: 1, 3: 3}

# result
ret = 1
for i in range(2, N+1):
    ret = ret * 2 + 1
print(ret)

# process
proc = [(1, 3)]
for i in range(2, N+1):
    proc = [(p[e[0]], p[e[1]]) for e in proc] + [(1, 3)] + [(n[e[0]], n[e[1]]) for e in proc]
for e in proc:
    print(*e)