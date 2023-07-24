n1=int(input("Digite o primeiro termo "))
n2=int(input("Digite a razao "))
termos=0
contador1=0
contador2=0
tm=0
tm1=0
contador3=0
while tm!=-1:
    contador3+=1
    if contador3==1:
        while contador1<10:
            contador1 += 1
            if contador1==1:
                termos=n1
            else:
                termos+=n2
            print(termos,end=" » ")
    elif contador3>1:
        tm=int(input("\nDigite quaantos termos queres amais "))
        while contador2<tm:
            contador2+=1
            termos+=n2
            print(termos,end=" » ")
    contador2=0
print("FIM")






