n1=int(input("Digite um numero "))
n2=int(input("Digite um outro numero "))
n3=int(input("Digite mais um numero "))
n4=int(input("Digite um ultimo numero "))
n5=(n1,n2,n3,n4)
print(f"Voce digitou os seguintes numeros {n5} ")
print(f"O 9 apareceu {n5.count(9)} vezes")
if n5.count(3)>0:
    print(f"O numero 3 apareceu na posição {n5.index(3)+1}")
else:
    print(f"O numero 3 nao foi digitado ")
c1=0
for c in n5:
    if c%2==0:
        c1+=1
print(f"Foram digitados {c1} numeros pares")

