s=0
c1=0
menos=0
menorp=""
c2=0
while True:
    c2+=1
    n=str(input("Digite o nome do seu produto: "))
    p=int(input("Digite o valor do produto: "))
    c = str(input("Quer continuar(s/n) ")).strip().lower()[0]
    while c not in "sn":
        c=str(input("Quer continuar(s/n) ")).strip().lower()[0]
    s+=p
    if p>1000:
        c1+=1

    if c2==1:
        menos=p
        menorp = n
    if p<menos:
        menos=p
        menorp=n
    if c=="n":
        break
print(f"A soma dos produtos é {s}, Existem {c1} produtos que custam mais de 1000 euros e o produto mais barato é {menorp} e custa {menos} ")


