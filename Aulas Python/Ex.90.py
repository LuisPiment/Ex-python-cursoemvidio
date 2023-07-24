c={}
c["nome"]=str(input("Digite o seu nome: ")).strip()
c["media"]=float(input("Qual foi a sua media: "))
if c["media"]<=5:
    c["aprovação"]="Reprovado"
elif c["media"]<=7.5:
    c["aprovação"]="Recuperação"
else:
    c["aprovação"]="Aprovado"
print(f"O nome é {c['nome']} a sua media {c['media']} e ele foi {c['aprovação']}")