def palindrome(word: str) -> str:
    n = len(word)
    # skip the left side once when a mismatch occurs
    i, j, pseudo, palin = 0, n-1, 0, 1
    while i < j:
        if word[i] == word[j]:
            i += 1
            j -= 1
        elif word[i] != word[j]:
            if not pseudo:
                i += 1
                pseudo = 1
            else:
                palin = 0
                break
    if palin:
        if pseudo:
            return "1"
        return "0"
    # skip the right side once when a mismatch occurs
    i, j, pseudo, palin = 0, n-1, 0, 1
    while i < j:
        if word[i] == word[j]:
            i += 1
            j -= 1
        elif word[i] != word[j]:
            if not pseudo:
                j -= 1
                pseudo = 1
            else:
                palin = 0
                break
    if palin:
        if pseudo:
            return "1"
        return "0"
    return "2"


ans = []
T = int(input())
for _ in range(T):
    word = input()
    ans.append(palindrome(word))

print("\n".join(ans))