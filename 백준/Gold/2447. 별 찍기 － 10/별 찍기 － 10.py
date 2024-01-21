def star(k):
    if k == 1:
        return '*'

    pre = star(k//3)
    top = [line*3 for line in pre]
    mid = [line + ' '*(k//3) + line for line in pre]
    return top + mid + top

print('\n'.join(star(int(input()))))