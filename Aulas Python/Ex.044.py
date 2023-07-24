from time import sleep
vp=float(input("Digite o valor do produto "))
print("Calculando...")
sleep(2)
print("\033[1;32mEscolha o seu meio de pagamento de acordo com as seguintes escolhas:\nEscolha o numero 1 para o Pagamento á vista por dinheiro\nEscolha o numero 2 para o pagamento á vista por cartão\nEscolha o numero 3 para o pagamento parcelado por 2 vezes\nEscolha o numero 4 para o pagamento parcelado de 3 vezes ou mais\033[m ")
e=int(input("Escolha o meio de pagamento "))
if e==1:
    p=vp*0.90
elif e==2:
    p=vp*0.95
elif e==3:
    p=vp
elif e==4:
    p=vp*1.20
else:
    p="N ao pode ser calculado pois a sua forma de pagamento nao pode ser usada"
print("O preço do seu produto é {}".format(p))
