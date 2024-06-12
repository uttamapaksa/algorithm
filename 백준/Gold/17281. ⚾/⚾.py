from itertools import permutations


def baseball(hitters, inning):
    score = 0
    hitters.insert(3, 0)
    idx = 0
    while inning < n:

        out = 0
        one, two, three = 0, 0, 0 
        while out < 3:
            v = arr[inning][hitters[idx]]
            if v == 0:
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
        inning += 1

    global ans
    if ans < score:
        ans = score


n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
ans = 0

for hitters in permutations([1, 2, 3, 4, 5, 6, 7, 8]):
    baseball(list(hitters), 0)

print(ans)