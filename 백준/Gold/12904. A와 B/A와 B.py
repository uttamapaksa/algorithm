s,t=[*input()],[*input()]
while len(s)<len(t):
  if t.pop()=='B':t=t[::-1]
print(int(s==t))