t=[]
for c in range(0,5):
    n1=int(input("Digite um numero "))
    if c==0 or n1>t[-1]:
        t.append(n1)
    else:
        pos=0
        while pos<len(t):
            if n1<=t[pos]:
                t.insert(pos,n1)
                break
            pos+=1
print(t)


