print("\033[1;33mAprovação de ano\033[m")
n1=float(input("Digite a sua priemira nota "))
n2=float(input("Digite a sua segunda nota "))
m=(n1+n2)/2
if m<5:
    ap="Reprovado"
elif 6.9>m>5:
    ap="Recuperação"
else:
    ap="Aprovado"
print("Foste de {} com media de {}".format(ap,m))

