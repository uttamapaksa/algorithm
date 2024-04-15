def solution(s):
    s = list(s)
    space = 1

    for i in range(len(s)):
        if s[i] == " ":
            space = 1
            continue
        if space:
            if ord(s[i]) >= 97:
                s[i] = chr(ord(s[i]) - 32)
            space = 0
        else:
            if ord(s[i]) <= 90:
                s[i] = chr(ord(s[i]) + 32)

    return "".join(s)