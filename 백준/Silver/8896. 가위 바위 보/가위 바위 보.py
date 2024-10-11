ans = []

for _ in range(int(input())):
    N = int(input())
    robots = {}
    for id in range(1, N+1):
        robots[id] = tuple(input())

    for round in range(len(robots[1])):
        union = {robots[id][round] for id in robots}
        if len(union) != 2:
            continue
        diff = tuple(*({'R', 'S', 'P'} - union))[0]
        lose = {'R': 'P', 'S': 'R', 'P': 'S'}[diff]
        loses = [id for id in robots if robots[id][round] == lose]
        for id in loses:
            del robots[id]

    if len(robots) > 1:
        ans.append(0)
    else:
        ans.append(tuple(robots.keys())[0])

print('\n'.join(map(str, ans)))