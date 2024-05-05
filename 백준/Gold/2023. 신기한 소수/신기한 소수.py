def is_prime(k):
    k = int(k)
    if k == 1:
        return 0
    if k <= 3:
        return 1
    for i in range(2, int(k**0.5) + 1):
        if not k % i:
            return 0
    return 1


def dfs(k, d):
    if d == N:
        ans.append(k)
        return
    for i in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        nk = k + i
        if is_prime(nk):
            dfs(nk, d+1)


N = int(input())
ans = []
dfs('', 0)
print("\n".join(ans))