inicio1=0
fim1=0
passo1=0
def contador(inicio,fim,passo):
    if passo<0:
        passo1=passo*-1
    elif passo==0:
        passo1=1
        passo=1
    else:
        passo1=passo
    if fim>inicio:
        inicio1=inicio
        fim1=fim
    elif inicio>fim:
        fim1 = fim-2
        inicio1=inicio
        if passo<0:
            passo=passo
        elif passo>0:
            passo=passo*-1
    print("-="*15)
    print(f"Contagem de {inicio} até {fim} de {passo1} em {passo1}")
    for c in range(inicio1,fim1+1,passo):
        print(c,end=" ")
    print("\n")
    print("-="*15)
contador(1,10,1)
contador(10,0,2)
print("Agora sua vez de personalizar: ")
i=int(input("Inicio: "))
f=int(input("Fim: "))
p=int(input("Passo: "))
contador(i,f,p)

