def fact(N):
    if not N:
        return 1
    return N * fact(N-1)

print(fact(int(input())))