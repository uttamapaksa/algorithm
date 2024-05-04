from itertools import combinations

def sol():
    if K < 0:
        return 0

    # words except 'a, n, t, i, c'
    antatica = {'a', 'n', 't', 'i', 'c'}
    words = []
    for _ in range(N):
        word = set()
        for c in input():
            if c not in antatica:
                word.add(c)
        words.append(word)

    # all inputted alphabets
    total = set()
    for word in words:
        total |= word

    # can teach any alphabet
    if len(total) <= K:
        return N

    # all combinations of inputted alphabets
    ans = 0
    for comb in combinations(total, K):
        comb = set(comb)
        tmp = 0
        for word in words:
            if word.issubset(comb):
                tmp += 1
        if ans < tmp:
            ans = tmp
    return ans


N, K = map(int, input().split())
K -= 5
print(sol())