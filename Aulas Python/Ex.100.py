import random
l=[]
def aleatorios(a,b):
    for c in range (0,6):
        l.append(random.randint(a,b))
    print(f"Os numeros randomizados foram {l}")
def pares(num):
    s=0
    for t in num:
        if t%2==0:
            s+=t
    print(f"A soma dos numeros pares de {l} é {s}")
aleatorios(1,10)
pares(l)




