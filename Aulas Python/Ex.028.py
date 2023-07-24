import random
print("Tente advinhar o numero que o pc esta a pensar de 0 a 5")
print("="*60)
p1=int(input("Digite o seu numero "))
p2=random.randint(0,5)
if p1==p2:
    print("O jogador ganhou")
else:
    print("A maquina ganhou ")
    print("Boa tentativa, a maquina escolheu {}".format(p2))
print("="*60)

print("Vamos jogar de novo?")

