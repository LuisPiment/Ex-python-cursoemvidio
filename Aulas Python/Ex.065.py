r=""
s=0
c=0
m=0
maior=0
menor=0
while r!="n":
    n1=int(input("Digite um numero "))
    r=str(input("Queres continuar(s/n) ")).strip().lower()[0]
    c+=1
    if c==1:
        menor=n1
    s+=n1
    m=s/c
    if n1>maior:
        maior=n1

    if n1<menor :
        menor=n1
print("O maior numero é {} e o menor é {}\n Voce digitou {} e a media deles é {:.2f}".format(maior,menor,c,m))
