u=[]
m1=[]
while True:
    nome=str(input("Digite o nome do aluno:"))
    n1=float(input("Digite a sua 1 nota: "))
    n2=float(input("Digite a sua 2 nota: "))
    c=str(input("Quer continuar: ")).strip().lower()[0]
    m=(n1+n2)/2
    m1.append(m)
    u.append([nome,[n1,n2]])
    if c =="n":
        break
for c in range(0,len(u)):
    print("-=-"*30)
    print("Nº    Nome       Media")
    print(f"{c}     {u[c][0]}      {m1[c]}")
while True:
    mo=int(input("Mostrar notas de qual aluno?(999 para parar):  "))
    if mo==999:
        break
    print(f"Notas do {u[mo][0]} {u[mo][1]}")
print("Espero que tenha gostado")


