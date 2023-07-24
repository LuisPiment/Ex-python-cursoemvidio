n1=int(input("Digite o numero inicial "))
n2=int(input("Digite a razão "))
contador=0
re=0
while contador<10:
    contador+=1
    if contador==1:
        re=n1
    else:
        re+=n2
    print(re,end=" » ")
print("FIM")



