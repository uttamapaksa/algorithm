def baseball():
    score = 0
    idx = 0
    for inning in range(n):
        out = 0
        one, two, three = 0, 0, 0
        while out < 3:
            v = arr[inning][hitters[idx]]
            if not v :
                out += 1
            elif v == 1:
                score += three
                one, two, three = 1, one, two 
            elif v == 2:
                score += two + three
                one, two, three = 0, 1, one 
            elif v == 3:
                score += one + two + three
                one, two, three = 0, 0, 1 
            else:
                score += one + two + three + 1
                one, two, three = 0, 0, 0 

            idx += 1
            if idx == 9:
                idx = 0

    global ans
    if ans < score:
        ans = score


def perm(k):
    if k == 3:
        perm(k+1)
        return
    if k == 9:
        baseball() 
        return
    for i in (1, 2, 3, 4, 5, 6, 7, 8):
        if visit[i]: continue
        visit[i] = 1
        hitters[k] = i
        perm(k+1)
        visit[i] = 0


n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
visit = [0] * 9
hitters = [0] * 9
ans = 0

perm(0)
print(ans)