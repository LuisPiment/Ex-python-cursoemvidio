n=("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezasseis","dezassete","dezeoito","dezanove","vinte")
n1=int(input("Digite um numero entre 0 e 20: "))
while True:
    if n1<0 or n1>20:
        n1 = int(input(" ERRO, Digite novamente um numero entre 0 e 20: "))
    else:
        break
print(f"O seu numero em extenso é {n[n1]}")