arr = [int(input()) for _ in range(int(input()))]
mxv = max(arr)  

pn = [1] * (mxv+1)
pn[0] = pn[1] = 0
for i in range(2, int(mxv**0.5)+1):
    for j in range(i*i, mxv+1, i):
        if pn[j]:
            pn[j] = 0

for v in arr:
    cnt = 0
    for i in range(2, v//2+1):
        if pn[i] and pn[v-i]:
            cnt += 1
    print(cnt)