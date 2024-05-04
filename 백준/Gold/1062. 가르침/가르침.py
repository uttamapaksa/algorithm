from itertools import combinations


def sol():
    if K < 0:
        return 0

    antatica = {'a', 'n', 't', 'i', 'c'}
    words = []  # all words convert to numbers
    total = set()  # all inputted alphabets
    for _ in range(N):
        word = 0
        for c in input():
            if c not in antatica:  # except 'a, n, t, i, c'
                word |= 1 << ord(c) - 97
                total.add(1 << ord(c) - 97)
        words.append(word)

    # can teach any alphabet
    if len(total) <= K:
        return N

    # all combinations of inputted alphabets
    ans = 0
    for comb in combinations(total, K):
        tmp = 0
        comb = sum(comb)
        for word in words:
            if comb & word == word:
                tmp += 1
        if ans < tmp:
            ans = tmp
    return ans


N, K = map(int, input().split())
K -= 5
print(sol())