print("Sequencia de fibonnaci")
n1=int(input("Quantos termos queres "))
contador=0
f1=0
f2=1
print(f1,f2,end=" ")
if n1%2==0:
    n1=(n1-3)/2
else:
    n2=((n1-3)/2)
while contador<n2:
    contador+=1
    f1=f1+f2
    f2=f1+f2
    print(f1,f2,end=" ")


