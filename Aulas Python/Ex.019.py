import random
p1=str(input("Diga o nome do primeiro aluno "))
p2=str(input("Diga o nome do segundo aluno "))
p3=str(input("Diga o nome do terceiro aluno "))
p4=str(input("Diga o nome do quarto aluno "))
s=(p1,p2,p3,p4)
p=random.choice(s)
print("O aluno escolhido foi {}".format(p))


