t=[]

while True:
    t.append(int(input("Digite um numero: ")))
    c=str(input("Quer continuar(S/N): ")).lower().strip()[0]
    if c=="n":
        break
if 5 in t:
    print("O 5 esta presente na sua lista")
else:
    print("O cinco nao esta presente na sua lista")
print(f"A sua lista contem {len(t)} numeros")
t.sort(reverse=True)
print(f"A sua lista por ordem decrescente fica {t}")
