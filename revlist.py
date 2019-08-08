N=int(input())
x=[int(x) for x in input().split()]
if len(x)==N:
    x=x[::-1]
    z=''
    a=''
    y=[]
    for i in range(len(x)):
        z=z+str(x[i])+'->'
    for i in range(len(z)):
        y.append(z[i])
        if i==len(z)-1 or i==len(z)-2:
            y[i]=''
    for i in range(len(y)):
        a=a+str(y[i])
    print(a)
    
