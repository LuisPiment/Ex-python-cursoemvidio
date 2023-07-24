from uteis import moeda
n1=float(input("Digite um numero: "))
print(f"A metade de {(n1)} é {moeda.metade(n1)}")
print(f"O dobro de {(n1)} é {moeda.dobro(n1)}")
print(f"Aumentado 10%, temos {moeda.aumentar(n1,10):.2f}")
print(f"Reduzindo 13%, temos {moeda.diminuir(n1,13):.2f}")