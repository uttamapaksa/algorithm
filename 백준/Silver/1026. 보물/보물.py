N = int(input())
arr1 = sorted(map(int, input().split()))
arr2 = sorted(map(int, input().split()), reverse=True)

answer = sum(arr1[i] * arr2[i] for i in range(N))
print(answer)