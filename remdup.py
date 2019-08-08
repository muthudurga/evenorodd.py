S=input()
a=[]
for i in range(len(S)):
    if S[i] not in a:
        a.append(S[i])
y=''
for i in range(len(a)):
    y=y+a[i]
print(y)
