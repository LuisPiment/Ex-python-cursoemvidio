from uteis import moeda
n1=float(input("Digite um numero: "))
print(f"A metade de {moeda.bonito(n1)} é {moeda.metade(n1,True)}")
print(f"O dobro de {moeda.bonito(n1)} é {moeda.dobro(n1,True)}")
print(f"Aumentado 10%, temos {moeda.aumentar(n1,10,True)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(n1,13,True)}")