def ficha(nome="Desconhecido",golos=0):
    print(f"O jogador {nome} fez {golos} golos")


n1=str(input("Digite o nome do jogador: ")).strip()
n2=str(input("Quantidade de golos: "))
if n2.isnumeric():
    n2=n2
else:
    n2=0
ficha(n1,n2)