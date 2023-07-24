np = []
np2 = []
nmai=[]
nmen=[]
c3=0
maior=0
menor=0
while True:
    np.append(str(input("Digite um nome: ")))
    np.append(int(input("Digite o seu peso: ")))
    c=str(input("Quer continuar: ")).strip().lower()[0]
    if len(np2)==0:
        menor=maior=np[1]
    else:
        if np[1] > maior:
            maior = np[1]
        if np[1] < menor:
            menor = np[1]
    np2.append(np[:])
    np.clear()
    c3+=1
    if c=="n":
        break
c1=0
for c2 in np2:
    if maior==c2[1]:
        nmai.append(c2[0])
    if menor==c2[1]:
        nmen.append(c2[0])
print(f"O maior peso foi {maior} e as pessoas que tiveram esse peso foram {nmai}")
print(f"O menor peso foi {menor} e as pessoas que tiveram esse peso foram {nmen}")
print(f"Foram registrados {c3} pessoas")




