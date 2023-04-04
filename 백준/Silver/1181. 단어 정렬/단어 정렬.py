a = int(input())

words_dict = {}

for i in range(a):
    b = input()
    words_dict[b] = len(b)

sorted_dict = sorted(words_dict.items(), key=lambda x: (x[1], x[0]))

for i in sorted_dict:
    print(i[0])