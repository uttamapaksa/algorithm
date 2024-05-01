def check():
    for i in range(N-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            return "NO"
    return "YES"


answer = []
tc = int(input())
for _ in range(tc):
    N = int(input())
    arr = [[*map(int, [*input()])] for _ in range(N)]
    arr.sort()
    answer.append(check())

print("\n".join(answer))