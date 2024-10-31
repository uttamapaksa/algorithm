a, b = map(int, input().split())
if a > 2*b or a <= b:
    print('NO')
else:
    print('YES')
    diff = a-b-1
    ans = ['aba']*diff
    ans.append('a'+'ba'*(b-diff))
    print(len(ans))
    print('\n'.join(ans))