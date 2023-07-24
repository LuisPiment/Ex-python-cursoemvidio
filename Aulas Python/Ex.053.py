f=str(input("Digite uma palavra ")).lower().strip()
i=f.split()
j="".join(i)
n=(j[::-1])
if j==n:
    print("A sua frase é Polindromo")

else:
    print("A sua frase nao é um polindromo")
print(n)
