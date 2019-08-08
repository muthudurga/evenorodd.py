N,K=input().split()
z=[int(z) for z in input().split()]
x=int(N)
y=int(K)
if len(z)==x:
    a=[]
    for i in range(len(z)):
        j=i+1
        if i!=len(z)-1:
            for j in range(1,len(z)):
                b=z[i]+z[j]
                if b==y:
                    a.append(y)
                    break
    if a!=[]:
        print('YES')
    else:
        print('NO')
