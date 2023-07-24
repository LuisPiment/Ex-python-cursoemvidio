from random import choice
print("Jogo de Pedra, papel e tesoura contra a cpu")
print("Escolha a sua jogada de acordo com as seguintes escolhas:\nEscolha o numero 1 para Tesoura\nEscolha o numero 2 para Pedra\nEscolha o numero 3 para Papel")
p1=int(input("Escolha o sua jogada "))
lista=(3,1,2)
cpu=choice(lista)
if p1==1 and cpu==2 or p1==2 and cpu==3 or p1==3 and cpu==1:
    tu="Perdeste"
elif p1==1 and cpu==3 or p1==2 and cpu==1 or p1==3 and cpu==2:
    tu= "Ganhaste"
elif p1==1 and cpu ==1 or p1==2 and cpu ==2 or p1==3 and cpu==3:
    tu="Empataste"
print("Tu {} o  pc escolheu {}".format(tu,cpu))





