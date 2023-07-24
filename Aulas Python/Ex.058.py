import random
print("Vamos jogar um jogo estou a pensar num numero entre 1 e 10 \nTens de tentar advinhar")
p1=int(input("Digite o seu numero  "))
pc=random.randint(1,10)
c=1
while p1!=pc:
    if pc>p1:
        c+=1
        p1=int(input(("Mais...Tente de novo ")))
    else:
        c+=1
        p1=int(input("Menos...Tente de novo "))
print("Voce acertou com {} Tentativas".format(c))

