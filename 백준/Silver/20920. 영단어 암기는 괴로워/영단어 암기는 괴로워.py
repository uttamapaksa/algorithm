N, M = map(int, input().split())
words = {}

for _ in range(N):
    word = input()
    if len(word) < M:
        continue
    if word in words:
        words[word][0] += 1
    else:
        words[word] = [1, len(word)]

ans = [word for word, _ in sorted(words.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]))]
print('\n'.join(ans))