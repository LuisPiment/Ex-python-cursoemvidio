from uteis import moeda
n1=float(input("Digite um numero: "))
print(f"A metade de {moeda.bonito(n1)} é {moeda.bonito(moeda.metade(n1))}")
print(f"O dobro de {moeda.bonito(n1)} é {moeda.bonito(moeda.dobro(n1))}")
print(f"Aumentado 10%, temos {moeda.bonito(moeda.aumentar(n1,10))}")
print(f"Reduzindo 13%, temos {moeda.bonito(moeda.diminuir(n1,13))}")