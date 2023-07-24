lista=[]
dic={}
mulheres=[]
media=0
soma=0
while True:
    dic["nome"]=str(input("Digite o seu nome: "))
    sex=str(input("Digite o seu sexo[M/F]: ")).lower().strip()[0]
    while sex not in  "fm":
        sex=str(input("Digite o seu sexo[M/F]: ")).lower().strip()[0]
    dic["sexo"]=sex
    id=int(input("Digite a sua idade: "))
    soma+=id
    dic["idade"]=id
    co=str(input("Quer continuar[S/N]: ")).strip(  ).lower()[0]
    while co not in "sn":
        co = str(input("Quer continuar[S/N]: ")).strip().lower()[0]
    lista.append(dic.copy())
    if co=="n":
        break
media=soma/len(lista)
print("-="*30)
print(f"Temos {len(lista)} pessoas cadastradas")
print("-="*30)
print(f"A media das idades é {media:.2f}")
print("-="*30)
print("As pessoas que estao acima da media sao:")
for l in lista:
            if l['idade']>media:
                print(f"Nomes= {l['nome']}; Sexo= {l['sexo']}; Idade= {l['idade']} ")
print("-="*30)
print("As mulheres sao:")
for l in lista:
    if l["sexo"]=="f":
        print(l["nome"])







