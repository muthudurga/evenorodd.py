S=input()
x=[]
for i in range(len(S)):
    x.append(S[i])
for i in range(len(x)):
    k=len(x)-1
    if x[k]==S[i]:
        x.pop()
        k=k-1
if x==[]:
    print('YES')
else:
    print('NO')
