s1=0
c1=0
n1="s"
imaior=0

for c in range (1,6):
    print("-" * 20)
    print(" " * 3, "Player {}".format(c), " " * 3)
    n = str(input("Qual o seu nome? "))
    s = str(input("Qual o seu sexo(f/m)? ")).strip().lower()
    i = int(input("Qual a sua idade? "))
    s1+=i/4
    if s=="m" and i>imaior:
        imaior=i
        n1=n
    if i<20 and s=="f":
        c1+=1

print("A media das idades é {}".format(s1))
print("O homem mais velho tem {} anos e chama-se {}".format(imaior,n1))
print("A quantidade de mulheres com menos de 20 anos é {}".format(c1))
