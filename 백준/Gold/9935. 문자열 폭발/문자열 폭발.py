text, pattern, ret = input(), [*input()], []
m, l = len(pattern), len(ret)
match_range = range(-m, 0)

for s in text:
    ret.append(s)
    l += 1
    go = 1
    while l >= m and go:
        for i in match_range:
            if ret[i] != pattern[i]:
                go = 0
                break
        else:
            for _ in match_range:
                ret.pop()
            l -= m

print(''.join(ret) or 'FRULA')