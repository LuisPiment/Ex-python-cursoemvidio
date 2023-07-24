import datetime
dt=datetime.date.today().year
pm=0
pme=0
for c in range(0,7):
    n=int(input("Digite o seu ano de nascimento "))
    n1=dt-n
    if n1>=18:
        pm+=1
    elif n1<18:
        pme+=1
print("Neste grupo tem {} de maior de idade \nNeste grupo tem {} menores de idade ".format(pm,pme))
