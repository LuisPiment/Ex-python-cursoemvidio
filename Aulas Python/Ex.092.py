import datetime
da=datetime.date.today().year
dados={}
dados["nome"]=str(input("Digite o sue nome "))
dn=int(input("Digite a sua data de nacimento "))
dados["idade"]=da-dn
dados["ctps"]=int(int(input("Digite a sua carteira de trabalho(0 se nao tiver) ")))
if dados["ctps"]!=0:
    dados["contratação"]=int(input("Qual ano foste contratado "))
    dados["salario"]=int(input("Qual o seu salario: "))
    dados["aposentadoria"]=((dados["contratação"]+35)-da)+dados["idade"]
print("-="*30)
for k,v in dados.items():
    print(f"O {k} tem valor de {v}")


