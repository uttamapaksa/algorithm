def solution():
    n = int(input())
    arr = input().split()

    if n >= 33:
        return 0
    minv = 8
    for i in range(n-2):
        A = arr[i]
        for j in range(i+1, n-1):
            B = arr[j]
            for k in range(j+1, n):
                minv = min(minv, (len(set(A + B + arr[k]))))
    return (minv - 4) * 2

for _ in range(int(input())):
      print(solution())