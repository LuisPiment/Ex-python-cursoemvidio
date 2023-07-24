j={}
l=[]
l2=0
j["nome"]=str(input("Nome do jogador: "))
j1=int(input(f"Quantos jogos o {j['nome']} jogou? "))
print("-="*30)
for c in range (1,j1+1):
    l3=(int(input(f"Quantos golos na partida {c} ")))
    l2+=l3
    l.append(l3)
j["golos"]=(l.copy())
j["total"]=l2
print("-="*30)
print(j)
print("-="*30)
for v,j in j.items():
    print(f"O campo {v} tem valor {j}")
print("-="*30)
for c1,c2 in enumerate(l):
    print(f"Na partida {c1+1} fez {c2} gols")
print(f"Foi um total de {l2} golos")
print("-=" * 30)