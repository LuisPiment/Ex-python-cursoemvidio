cont=0
n1=int(input("Digite um numero "))
for c in range(2,n1):
    if n1%c==0:
        cont+=1
if cont==0:
    print("O seu numero é primo")
else:
    print("O seu numero nao é primo")



