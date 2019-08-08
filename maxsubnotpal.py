S=input()
x=[]
for i in range(len(S)):
    x.append(S[i])
for i in range(len(x)):
    k=len(x)-1
    if x[k]==S[i]:
        x.pop()
        k=k-1
if x!=[]:
    print(S)
else:
    y=[]
    for i in range(len(S)):
        if i!=len(S)-1:
            y.append(S[i])
    a=''
    for i in range(len(y)):
        a=a+y[i]
    print(a)
