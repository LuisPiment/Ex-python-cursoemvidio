c1=c2=c3=0
while True:
    n=int(input("Digite a sua idade "))
    se=str(input("Digite o seu sexo (f/m): ")).strip().lower()[0]
    while se not in "fm":
        se = str(input("Digite o seu sexo (f/m): ")).strip().lower()[0]
    con=str(input("Quer continuar[s/n]: ")).strip().lower()[0]
    while con not in "sn":
        con = str(input("Quer continuar?(s/n): ")).strip().lower()[0]
    print(20*"-=-")
    if n>18:
        c1+=1
    if se=="m":
        c2+=1
    if n<20 and se=="f":
        c3+=1
    if con=="n":
        break
print(f"Tiveram {c1} maiores de idade\nExistem {c2} homens\nExistem {c3} mulheres com menos de 20 anos")





