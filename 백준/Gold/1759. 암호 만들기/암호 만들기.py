L, C = map(int, input().split())
chars = sorted([*input().split()])
vowelset = {'a', 'e', 'i', 'o', 'u'}

def sol(substr, vowel, conso, k):
    if vowel + conso == L:
        if vowel and conso >= 2:
            print(substr)
        return
    
    for i in range(k, C):
        if chars[i] in vowelset:
            sol(substr + chars[i], vowel+1, conso, i+1)
        else:
            sol(substr + chars[i], vowel, conso+1, i+1)

sol('', 0, 0, 0)