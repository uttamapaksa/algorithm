N = int(input())
if N % 2:
    print(0)
else:
    w, s = 1, 3
    for _ in range((N//2)-1):
        w, s = s+w, w*2 + s*3
    print(s)