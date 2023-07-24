n1=0
contador=0
s=0
while n1!=999:
    n1=int(input("Digite um numero(digite 999para parar) "))
    s+=n1
    contador+=1
print("A soma dos seus numeros é {} e voce digitou {} numeros".format(s-999,contador-1))