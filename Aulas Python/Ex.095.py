tjogo=[]
jogo={}
l=[]
l2=c0=c1=0
continuar=""
while True:
    jogo["nome"]=str(input("Nome do jogador: "))
    j1=int(input(f"Quantos jogos o {jogo['nome']} jogou? "))
    print("-="*30)
    for c in range (1,j1+1):
        l3=(int(input(f"Quantos golos na partida {c} ")))
        l2+=l3
        l.append(l3)
    jogo["golos"]=(l.copy())
    jogo["total"]=l2
    tjogo.append(jogo.copy())
    continuar=str(input("Quer continuar(s/n)? ")).lower().strip()[0]
    l.clear()
    jogo.clear()
    if continuar in "n":
        break
print("-=" * 30)
print(f"{'Cod':<} {'Nome':^12} {'Golos':^12} {'Total de Golos':>25}")
for l in tjogo:
        print(f"{c0}      {l['nome']}           {l['golos']}                {l['total']}")
        c0+=1
print("-="*30)
while True:
    j2=int(input("Qual jogador quer ver?(999 parar): "))
    c=0
    if j2==999:
        break
    if j2<len(tjogo):
        print(f"Levantamento do jogador {tjogo[j2]['nome']} ")
        for k0 in tjogo[j2]["golos"]:
            c1+=1
            print(f"No jogo {c1} ele fez {k0}")
    else:
        print("Esse numero de jogador nao existe")









