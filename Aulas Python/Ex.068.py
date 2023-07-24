import random
c=0
while True:
    cpu=random.randint(1,10)
    n=int(input(("Vamos jogar par ou impar\nDigite o seu numero ")))
    p=str(input("Digite par ou impar ")).strip().lower()[0]
    while p not in "ip":
        p = str(input("Digite par ou impar ")).strip().lower()[0]
    r=n+cpu
    if r%2==0 and p=="i":
        v="perdeu"
        ip="par"
    elif r%2!=0 and p=="i":
        v="ganhou"
        ip="impar"
        c+=1
    elif r%2==0 and p=="p":
        v="ganhou"
        ip="par"
        c+=1
    elif r%2!=0 and p=="p":
        v="perdeu"
        ip="impar"
    print(30*"-=-")
    print(f"Voce {v} pois escolheu {n} e a cpu escolheu {cpu}\nPois a soma de {n} e {cpu} é {r} e isso é {ip} ")
    print(30 * "-=-")
    if v=="perdeu":
        break
print(f"Acabou pois voce PERDEU espero que tenha gostado voce ganhou {c} vezes")





