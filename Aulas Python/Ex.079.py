num=[]
while True:
    n=int(input("Digite um numero "))

    if n not in num:
        num.append(n)
        print("Irei adcionar a lista")
    else:
        print("Numero duplicao, nao irei adcionar")
    c = str(input("Quer continuar(S/N): ")).strip().upper()[0]
    if c=="N":
        break
num.sort()
print(f"Os numero digitados foram {num}")
