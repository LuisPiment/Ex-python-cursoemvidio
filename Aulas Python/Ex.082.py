n=[]
p=[]
i=[]
while True:
    n1=int(input("Digite um numero "))
    c=str(input("Quer continuar(S/N): ")).strip().lower()[0]
    n.append(n1)
    if n1%2==0:
        p.append(n1)
    else:
        i.append(n1)
    if c=="n":
        break
n.sort()
p.sort()
i.sort()
print(f"Os numeros digitados foram {n}\nOs nuemros pares sao {p}\nOs numeros impares sao {i} ")